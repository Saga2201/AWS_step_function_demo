import json
import os

import boto3
from dotenv import load_dotenv

load_dotenv()

os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
os.environ['AWS_DEFAULT_REGION'] = os.getenv('AWS_DEFAULT_REGION')


sfn_client = boto3.client('stepfunctions')
state_machine_arn = 'arn:aws:states:ap-south-1:843379814955:stateMachine:ProcessTransactionStateMachine'
response = sfn_client.start_execution(
    stateMachineArn=state_machine_arn,
    name='test4',
    input=json.dumps({'TransactionType': 'PURCHASE'})
)
print(response)
