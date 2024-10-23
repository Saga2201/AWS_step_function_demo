import os

import boto3
from dotenv import load_dotenv

load_dotenv()

os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
os.environ['AWS_DEFAULT_REGION'] = os.getenv('AWS_DEFAULT_REGION')

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda', region_name='ap-south-1')
with open('process_purchase.zip', 'rb') as f:
    process_purchase_zip = f.read()
with open('process_refund.zip', 'rb') as f:
    process_refund_zip = f.read()

role = iam_client.get_role(RoleName='LambdaBasicExecution')

process_purchase_response = lambda_client.create_function(
    FunctionName='process_purchase',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='process_purchase.lambda_handler',
    Code=dict(ZipFile=process_purchase_zip),
    Timeout=300,  # Maximum allowable timeout
)
process_refund_response = lambda_client.create_function(
    FunctionName='process_refund',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='process_refund.lambda_handler',
    Code=dict(ZipFile=process_refund_zip),
    Timeout=300,  # Maximum allowable timeout
)
print(process_purchase_response)
print(process_refund_response)