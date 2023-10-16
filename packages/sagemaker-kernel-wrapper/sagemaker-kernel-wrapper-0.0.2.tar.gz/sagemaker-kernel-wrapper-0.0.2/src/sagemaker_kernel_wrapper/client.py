import boto3

STAGE_MAPPING = {"devo": "beta", "loadtest": "gamma"}


class SageMakerClient:
    @staticmethod
    def create_instance(region_name=None, stage=None):
        create_client_args = {"service_name": "sagemaker", "region_name": region_name}

        if stage and region_name and stage != "prod":
            endpoint_stage = STAGE_MAPPING[stage.lower()]
            create_client_args[
                "endpoint_url"
            ] = f"https://sagemaker.{endpoint_stage}.{region_name}.ml-platform.aws.a2z.com"

        session = boto3.session.Session()
        return session.client(**create_client_args)
