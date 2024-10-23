# This script will deploy step function to AWS

import json
import os

import boto3
from dotenv import load_dotenv

load_dotenv()

os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
os.environ['AWS_DEFAULT_REGION'] = os.getenv('AWS_DEFAULT_REGION')

sfn_client = boto3.client('stepfunctions')
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')
process_purchase_lambda = lambda_client.get_function(
    FunctionName='process_purchase'
)
process_refund_lambda = lambda_client.get_function(
    FunctionName='process_refund'
)
role = iam_client.get_role(RoleName='LambdaBasicExecution')
process_purchase_arn = process_purchase_lambda['Configuration']['FunctionArn']
process_refund_arn = process_refund_lambda['Configuration']['FunctionArn']

asl_definition = {
    'Comment': 'Transaction Processor State Machine',
    'StartAt': 'ProcessTransaction',
    'States': {
        'ProcessTransaction': {
            'Type': 'Choice',
            'Choices': [
                {
                    'Variable': '$.TransactionType',
                    'StringEquals': 'PURCHASE',
                    'Next': 'ProcessPurchase'
                },
                {
                    'Variable': '$.TransactionType',
                    'StringEquals': 'REFUND',
                    'Next': 'ProcessRefund'
                }
            ]
        },
        'ProcessPurchase': {
            'Type': 'Task',
            'Resource': process_purchase_arn,
            'End': True
        },
        'ProcessRefund': {
            'Type': 'Task',
            'Resource': process_refund_arn,
            'End': True
        }
    }
}

response = sfn_client.create_state_machine(
    name='ProcessTransactionStateMachine',
    definition=json.dumps(asl_definition),
    roleArn=role['Role']['Arn']
)
print(response)