import os
import sys

import json
import logging
import boto3

from sagemaker_kernel_wrapper.client import SageMakerClient
from sagemaker_kernel_wrapper.metadata import AppMetadata, InternalMetadata
from sagemaker_kernel_wrapper.resource_tag import ResourceTagRetriever

AWS_GLUE_TAGS = "glue_tags"

logging.basicConfig()
logger = logging.getLogger("sm_gis_wrapper")
logger.setLevel(logging.INFO)


def _get_tags_string():
    try:
        app_medata = AppMetadata()
        space_name = app_medata.get_space_name()
        user_profile = app_medata.get_user_profile_name()
        domain_id = app_medata.get_domain_id()
        region = app_medata.get_region_name()
        stage = InternalMetadata().get_stage()

        client = SageMakerClient.create_instance(region_name=region, stage=stage)
        tag_retriever = ResourceTagRetriever(client)
        user_or_space_tags = {}
        if len(user_profile) > 0:
            user_or_space_tags = tag_retriever.get_user_profile_tags(
                domain_id=domain_id, user_profile_name=user_profile
            )
        elif len(space_name) > 0:
            user_or_space_tags = tag_retriever.get_space_tags(
                domain_id=domain_id, space_name=space_name
            )

        domain_tags = tag_retriever.get_domain_tags(domain_id=domain_id)

        # lower level take precedence
        tags = {**domain_tags, **user_or_space_tags}

        return json.dumps(tags)
    except Exception as error:
        # catch all possible exceptions. Tagging related failure should not affect GIS kernel creation
        logger.warning(
            "Error while preparing SageMaker Studio tags. No tags from domain, user profile or space are propagated. "
            "This does not block Glue Interactive Session kernel launch and Glue session still functions. "
            f"Error: {error}"
        )
        # return empty map string so that no tag gets propagated to Glue
        return "{}"


def exec_kernel():
    tags_str = {}

    # the notebook job is running out of Studio and no tag propagation for notebook job for now.
    if "SM_JOB_DEF_VERSION" not in os.environ:
        tags_str = _get_tags_string()
        os.environ[AWS_GLUE_TAGS] = tags_str
        logger.info(f"AWS_GLUE_TAGS from SageMaker Studio: {tags_str}.")

    sys.argv[0] = sys.executable
    logger.info(f"Running Glue Kernel: {sys.argv} boto3 version: {boto3.__version__}")
    os.execvp(sys.argv[0], sys.argv)


if __name__ == "__main__":
    exec_kernel()
