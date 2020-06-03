# Next Caller VeriCall API for Amazon Connect

Cloudformation template and Python script to invoke Next Caller's VeriCall API via an Amazon Lambda function.

## Credentials

If you'd like to use the Next Caller VeriCall API please reach out to us at [https://nextcaller.com](https://nextcaller.com) to obtain credentials.

## Official API Documentation

Documentation for the Next Caller VeriCall API can be found at: [https://docs.nextcaller.com/vericall](https://docs.nextcaller.com/vericall/index.html)

## Connect Integration
Using the Amazon Connect Contact Flow you will need to store a few attributes as input parameters when invoking the function:

![FunctionSetup](./docs/images/lambda-input-parameters.png)

## Usage

Use `sam` to build, invoke and deploy the function.

##### SAM Build:
`sam build -b build -t aws/stack.yaml --use-container`

##### SAM Invoke:
There is sample event in the [example_event](example_event/) folder.

`sam local invoke -t build/template.yaml -e example_events/sample_score.json --parameter-overrides ParameterKey=LogLevel,ParameterValue=INFO ParameterKey=APIUsername,ParameterValue=REPLACE_ME ParameterKey=APIPassword,ParameterValue=REPLACE_ME`

##### SAM Deploy:
`sam deploy -t build/template.yaml --s3-bucket REPLACE_ME --stack-name REPLACE_ME --parameter-overrides ParameterKey=LogLevel,ParameterValue=INFO ParameterKey=APIUsername,ParameterValue=REPLACE_ME ParameterKey=APIPassword,ParameterValue=REPLACE_ME --capabilities CAPABILITY_IAM`
