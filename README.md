# AWS Step Function Demo

## Steps to Execute the AWS Step Function in This Repository

### 1. Create Lambda Functions Locally

- **1.1** Create `process_purchase.py`.
- **1.2** Create `process_refund.py`.
- **1.3** Prepare a ZIP file containing both Python scripts.
- **1.4** Execute the `create_lambda_functions.py` script to create the Lambda functions in AWS.

### 2. Create IAM Role

- **2.1** Use the `create_invoke_role.py` script to create a role and attach the appropriate AWS policy to it.

### 3. Create Step Function

- **3.1** Use the `main.py` script to create the AWS Step Function.

### 4. Execute Step Function

- **4.1** Use the `execute_step_function.py` script to execute the Step Function.

### Sample `.env` File

```plaintext
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=
```

###### Make sure you have enough permission to execute the lambda within step function.
###### Add this permission on role which is attached with IAM uer.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": [
                "arn:aws:lambda:ap-south-1:843379814955:function:process_refund",
                "arn:aws:lambda:ap-south-1:843379814955:function:process_purchase"
            ]
        }
    ]
}
```