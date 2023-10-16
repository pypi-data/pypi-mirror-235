import unittest
from unittest.mock import Mock, patch
import json
import sys
import os

from sagemaker_kernel_wrapper.sm_gis_wrapper import _get_tags_string
from sagemaker_kernel_wrapper.sm_gis_wrapper import exec_kernel


class TestGetTagsString(unittest.TestCase):
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.AppMetadata")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.InternalMetadata")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.SageMakerClient")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.ResourceTagRetriever")
    def test_get_tags_string_user_profile(
        self,
        mock_tag_retriever,
        mock_sagemaker_client,
        mock_internal_metadata,
        mock_app_metadata,
    ):
        # Prepare mock data and responses
        app_metadata_instance = mock_app_metadata.return_value
        app_metadata_instance.get_space_name.return_value = ""
        app_metadata_instance.get_user_profile_name.return_value = "user-profile-123"
        app_metadata_instance.get_domain_id.return_value = "domain-123"
        app_metadata_instance.get_region_name.return_value = "us-west-2"

        mock_internal_metadata_instance = mock_internal_metadata.return_value
        mock_internal_metadata_instance.get_stage.return_value = "prod"
        mock_tag_retriever_instance = mock_tag_retriever.return_value

        mock_tag_retriever_instance.get_domain_tags.return_value = {
            "tag1": "value1",
            "tag2": "value2",
        }

        mock_tag_retriever_instance.get_user_profile_tags.return_value = {
            "tag2": "value2_override",
            "tag3": "value3",
        }

        # Call the function under test
        result = _get_tags_string()

        # Assert the expected result and interactions with dependencies
        self.assertEqual(
            result,
            json.dumps(
                {
                    "tag1": "value1",
                    "tag2": "value2_override",
                    "tag3": "value3",
                }
            ),
        )
        mock_tag_retriever.assert_called_once_with(
            mock_sagemaker_client.create_instance.return_value
        )
        mock_tag_retriever_instance.get_user_profile_tags.assert_called_once_with(
            domain_id="domain-123", user_profile_name="user-profile-123"
        )
        mock_tag_retriever_instance.get_domain_tags.assert_called_once_with(
            domain_id="domain-123"
        )

    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.AppMetadata")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.InternalMetadata")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.SageMakerClient")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.ResourceTagRetriever")
    def test_get_tags_string_space(
        self,
        mock_tag_retriever,
        mock_sagemaker_client,
        mock_internal_metadata,
        mock_app_metadata,
    ):
        # Prepare mock data and responses
        app_metadata_instance = mock_app_metadata.return_value
        app_metadata_instance.get_space_name.return_value = "myspace"
        app_metadata_instance.get_user_profile_name.return_value = ""
        app_metadata_instance.get_domain_id.return_value = "domain-123"
        app_metadata_instance.get_region_name.return_value = "us-west-2"

        mock_internal_metadata_instance = mock_internal_metadata.return_value
        mock_internal_metadata_instance.get_stage.return_value = "prod"
        mock_tag_retriever_instance = mock_tag_retriever.return_value

        mock_tag_retriever_instance.get_domain_tags.return_value = {
            "tag1": "value1",
            "tag2": "value2",
        }

        mock_tag_retriever_instance.get_space_tags.return_value = {
            "tag2": "value2_override",
            "tag3": "value3",
        }

        # Call the function under test
        result = _get_tags_string()

        # Assert the expected result and interactions with dependencies
        self.assertEqual(
            result,
            json.dumps(
                {
                    "tag1": "value1",
                    "tag2": "value2_override",
                    "tag3": "value3",
                }
            ),
        )
        mock_tag_retriever.assert_called_once_with(
            mock_sagemaker_client.create_instance.return_value
        )
        mock_tag_retriever_instance.get_space_tags.assert_called_once_with(
            domain_id="domain-123", space_name="myspace"
        )
        mock_tag_retriever_instance.get_domain_tags.assert_called_once_with(
            domain_id="domain-123"
        )


class TestExecKernel(unittest.TestCase):
    def setUp(self):
        self.original_env = dict(os.environ)

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.original_env)

    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper._get_tags_string")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.os")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.logger")
    def test_exec_kernel(self, mock_logger, mock_os, mock_get_tags_string):
        mock_get_tags_string.return_value = '{"key": "value"}'

        # Call the function under test
        exec_kernel()

        # Assert the expected interactions with dependencies
        mock_get_tags_string.assert_called_once()
        mock_os.environ.__setitem__.assert_called_once_with(
            "glue_tags", '{"key": "value"}'
        )
        mock_os.execvp.assert_called_once_with(sys.argv[0], sys.argv)
        mock_get_tags_string.assert_called_once_with()

    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper._get_tags_string")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.os")
    @patch("sagemaker_kernel_wrapper.sm_gis_wrapper.logger")
    def test_exec_kernel_for_simulated_job_case(
        self, mock_logger, mock_os, mock_get_tags_string
    ):
        mock_os.environ.__contains__.return_value = True
        exec_kernel()
        mock_os.execvp.assert_called_once_with(sys.argv[0], sys.argv)
        mock_get_tags_string.assert_not_called()
        mock_os.environ.__setitem__.assert_not_called()
