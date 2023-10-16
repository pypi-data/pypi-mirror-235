import json

# This is a public contract - https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-run-and-manage-metadata.html#notebooks-run-and-manage-metadata-app
APP_METADATA_FILE_LOCATION = "/opt/ml/metadata/resource-metadata.json"

# Internal metadata which is not part of public contract.
SAGEMAKER_INTERNAL_METADATA_FILE = "/opt/.sagemakerinternal/internal-metadata.json"


class AppMetadata:
    _instance = None

    def __init__(self, app_metadata=APP_METADATA_FILE_LOCATION):
        with open(app_metadata, "r") as file:
            self.metadata = json.load(file)

    # singleton to avoid unnecessary reloading
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def _get_app_arn(self) -> str:
        return self.metadata["ResourceArn"]

    def get_partition(self):
        return self._get_app_arn().split(":")[1]

    def get_region_name(self):
        return self._get_app_arn().split(":")[3]

    def get_aws_account_id(self):
        return self._get_app_arn().split(":")[4]

    def get_user_profile_name(self):
        return self.metadata.get("UserProfileName", "")

    def get_space_name(self):
        return self.metadata.get("SpaceName", "")

    def get_domain_id(self):
        return self.metadata.get("DomainId")


class InternalMetadata:
    _instance = None

    def __init__(self, app_metadata=SAGEMAKER_INTERNAL_METADATA_FILE):
        with open(app_metadata, "r") as file:
            self.metadata = json.load(file)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_stage(self) -> str:
        return self.metadata["Stage"]
