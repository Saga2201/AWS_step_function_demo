import json
import os

import boto3
from dotenv import load_dotenv

load_dotenv()

os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
os.environ['AWS_DEFAULT_REGION'] = os.getenv('AWS_DEFAULT_REGION')

iam = boto3.client('iam')

role_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
response = iam.create_role(
  RoleName='StepFunctionLambdaBasicExecution',
  AssumeRolePolicyDocument=json.dumps(role_policy),
)
attach_policy_response = iam.attach_role_policy(
    RoleName='StepFunctionLambdaBasicExecution',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaRole'
)
print(response)
print(attach_policy_response)