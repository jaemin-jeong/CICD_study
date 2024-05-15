import os
import json
import boto3

# from dotenv import load_dotenv

from botocore.exceptions import ClientError

from settings import development


# (dev)secret_name: CICD_STUDY_DEV
def get_secret(secret_name):
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name="ap-northeast-2",
        aws_access_key_id=development.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=development.AWS_SECRET_ACCESS_KEY,
    )

    try:
        secret_value_res = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    return json.loads(secret_value_res["SecretString"])
