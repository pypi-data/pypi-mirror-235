import os
from typing import Optional
from lightning_cloud.rest_client import LightningClient
from abc import ABC, abstractmethod
from pathlib import Path

# To avoid adding lightning_utilities as a dependency for now.
try:
    import boto3
    _BOTO3_AVAILABLE = True
except Exception:
    _BOTO3_AVAILABLE = False


class _Resolver(ABC):
    @abstractmethod
    def __call__(self, root: str) -> Optional[str]:
        pass


class _LightningSrcResolver(_Resolver):
    """The `_LightningSrcResolver` enables to retrieve a cloud storage path from a directory."""

    def __call__(self, root: str) -> Optional[str]:
        root_absolute = str(Path(root).absolute())

        if root_absolute.startswith("/teamspace/studios/this_studio"):
            return None

        if root_absolute.startswith("/.project/cloudspaces") and len(root_absolute.split("/")) > 3:
            return self._resolve_studio(root_absolute, None, root_absolute.split("/")[3])

        if root_absolute.startswith("/teamspace/studios") and len(root_absolute.split("/")) > 3:
            return self._resolve_studio(root_absolute, root_absolute.split("/")[3], None)

        if root_absolute.startswith("/teamspace/s3_connections") and len(root_absolute.split("/")) > 3:
            return self._resolve_s3_connections(root_absolute)

        return None

    def _resolve_studio(self, root: str, target_name: str, target_id: str) -> str:
        client = LightningClient()

        # Get the ids from env variables
        cluster_id = os.getenv("LIGHTNING_CLUSTER_ID", None)
        project_id = os.getenv("LIGHTNING_CLOUD_PROJECT_ID", None)

        if cluster_id is None:
            raise RuntimeError("The `cluster_id` couldn't be found from the environement variables.")

        if project_id is None:
            raise RuntimeError("The `project_id` couldn't be found from the environement variables.")

        clusters = client.cluster_service_list_clusters().clusters

        target_cloud_space = [
            cloudspace
            for cloudspace in client.cloud_space_service_list_cloud_spaces(
                project_id=project_id, cluster_id=cluster_id
            ).cloudspaces
            if cloudspace.name == target_name or cloudspace.id == target_id
        ]

        if not target_cloud_space:
            raise ValueError(f"We didn't find any matching Studio for the provided name `{target_name}`.")

        target_cluster = [cluster for cluster in clusters if cluster.id == target_cloud_space[0].cluster_id]

        if not target_cluster:
            raise ValueError(
                f"We didn't find a matching cluster associated with the id {target_cloud_space[0].cluster_id}."
            )

        bucket_name = target_cluster[0].spec.aws_v1.bucket_name

        return os.path.join(
            f"s3://{bucket_name}/projects/{project_id}/cloudspaces/{target_cloud_space[0].id}/code/content",
            *root.split("/")[4:],
        )

    def _resolve_s3_connections(self, root: str) -> str:
        client = LightningClient()

        # Get the ids from env variables
        project_id = os.getenv("LIGHTNING_CLOUD_PROJECT_ID", None)
        if project_id is None:
            raise RuntimeError("The `project_id` couldn't be found from the environement variables.")

        target_name = root.split("/")[3]

        data_connections = client.data_connection_service_list_data_connections(project_id).data_connections

        data_connection = [dc for dc in data_connections if dc.name == target_name]

        if not data_connection:
            raise ValueError(f"We didn't find any matching data connection with the provided name `{target_name}`.")

        return os.path.join(data_connection[0].aws.source, *root.split("/")[4:])


class _LightningTargetResolver(_Resolver):
    """The `_LightningTargetResolver` generates a cloud storage path from a directory."""

    def __call__(self, name: str) -> Optional[str]:
        # Get the ids from env variables
        cluster_id = os.getenv("LIGHTNING_CLUSTER_ID", None)
        project_id = os.getenv("LIGHTNING_CLOUD_PROJECT_ID", None)

        if cluster_id is None or project_id is None:
            return

        if not _BOTO3_AVAILABLE:
            return

        client = LightningClient()

        clusters = client.cluster_service_list_clusters().clusters

        target_cluster = [cluster for cluster in clusters if cluster.id == cluster_id]

        if not target_cluster:
            raise ValueError(f"We didn't find a matching cluster associated with the id {cluster_id}.")

        prefix = os.path.join(f"projects/{project_id}/optimized_datasets/", name)

        s3 = boto3.client("s3")

        objects = s3.list_objects_v2(
            Bucket=target_cluster[0].spec.aws_v1.bucket_name,
            Delimiter="/",
            Prefix=prefix + "/",
        )
        version = objects["KeyCount"] + 1 if objects["KeyCount"] else 0

        cloud_storage_path = os.path.join(f"s3://{target_cluster[0].spec.aws_v1.bucket_name}", prefix, f"version_{version}")

        print(f"Storing the files under {cloud_storage_path}")

        return cloud_storage_path