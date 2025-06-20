import boto3
import json

# Initialize the Bedrock runtime client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1') # Replace with your region

# Define the model ID for Meta Llama 3.1 8B Instruct
model_id = 'arn:aws:sagemaker:us-east-1:196856463470:endpoint/endpoint-quick-start-nwm3o'

# Prepare the input prompt
prompt = "Explain the significance of the water cycle in Earth's ecosystem."

# Construct the request body
body = {
"messages": [
    {
        "role": "system",
        "content": "You are a helpful assistant that answers in JSON ormat with a key 'message'."
    },
    {
        "role": "user",
        "content": "Tell me a fun fact about giraffes."
    },
],
"max_gen_len": 512,
"temperature": 0.7,
"top_p": 0.9
}

print(body)p_p": 0.9
}

# Invoke the model
response = bedrock.invoke_model(
modelId=model_id,
contentType='application/json',
accept='application/json',
body=json.dumps(body)
)

# Parse and print the response
response_body = json.loads(response['body'].read())
print(response_body)
