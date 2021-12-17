# Next Caller VeriCall API for Amazon Connect

Cloudformation template and Python script to invoke Next Caller's VeriCall API via an Amazon Lambda function.

## Credentials

If you'd like to use the Next Caller VeriCall API please reach out to us at [https://nextcaller.com](https://nextcaller.com) to obtain credentials.

## Official API Documentation

Documentation for the Next Caller VeriCall API can be found at: [https://docs.nextcaller.com/vericall](https://docs.nextcaller.com/vericall/index.html)

## Usage

You'll need the following information:

* VeriCall Username
* VeriCall Password
* Amazon Connect Instance ID

### Option 1 (GUI):

1. Upload `template.yaml` in your CloudFormation console and follow the prompts.

### Option 2 (CLI):

Use `sam` to build, invoke and deploy the function.

1. Download and setup SAM: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
2. Use `sam build` to build the application: 
`sam build -b build -t aws/cloudformation/stack.yaml --use-container`
3. In your Amazon account create an S3 bucket to upload the code to (you can use an existing one you have read/write access to).
4. Use `sam deploy` to deploy the application (remember to replace the `REPLACE_ME` with your information specific information): 
`sam deploy -t build/template.yaml --s3-bucket REPLACE_ME --stack-name REPLACE_ME --parameter-overrides ParameterKey=LogLevel,ParameterValue=INFO ParameterKey=APIUsername,ParameterValue=REPLACE_ME ParameterKey=APIPassword,ParameterValue=REPLACE_ME --capabilities CAPABILITY_IAM`

## Connect Integration
If you didn't use the CloudFormation template from earlier you'll need to update your Lambda Integration in your Amazon Connect Contact Flow to store a few attributes as input parameters when invoking the function:

![FunctionSetup](./docs/images/lambda-input-parameters.png)
