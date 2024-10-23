import boto3

# # Load the state machine definition
# with open('state_machine_definition.json') as f:
#     state_machine_definition = json.load(f)
#
# # Create the state machine
# response = client.create_state_machine(
#     name='HelloWorldStateMachine',
#     definition=json.dumps(state_machine_definition),
#     roleArn='arn:aws:iam::843379814955:user/Admin'
# )
#
# print("State Machine ARN:", response['stateMachineArn'])

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')
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