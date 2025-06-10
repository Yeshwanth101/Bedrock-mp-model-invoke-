import boto3

client = boto3.client('bedrock', region_name='us-east-1')

model_arn = "arn:aws:sagemaker:us-east-1:aws:hub-content/SageMakerPublicHub/Model/widn-tower-anthill/4.0.2"
endpoint_name = "widn_tower_anthill_ep"

response = client.create_marketplace_model_endpoint(
    modelSourceIdentifier=model_arn,
    endpointName=endpoint_name,
    endpointConfig={
        "sagemaker": {
            "initialInstanceCount": 1,
            "instanceType": "ml.m5.large",
            "executionRole": "arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_SAGEMAKER_ROLE"
        }
    },
    acceptEula=True
)

print("Endpoint ARN:", response["marketplaceModelEndpoint"]["endpointArn"])
print("Status:", response["marketplaceModelEndpoint"]["status"])


#### Invoke model
import boto3

# Initialize Bedrock client
client = boto3.client('bedrock', region_name='us-east-1')

# Specify model ARN after subscription
model_arn = "arn:aws:sagemaker:us-east-1:aws:hub-content/SageMakerPublicHub/Model/widn-tower-anthill/4.0.2"

# Example Input Payload (this depends on the model’s input format)
input_payload = {
    "input_data": "Some input to the model here"  # Adjust based on model’s input specification
}

# Invoke the model
response = client.invoke_model(
    ModelId=model_arn,
    Body=input_payload,
    ContentType="application/json"  # You may need to adjust the content type based on model expectations
)

# Process the response
print("Model response:", response['Body'].read().decode())
