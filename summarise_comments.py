import os
import boto3
import json

# Load the contents of the comments.txt file
with open('comments.txt', 'r') as file:
    file_contents = file.read()

# Create a Bedrock client
session = boto3.Session(region_name='us-east-1')
bedrock = boto3.client('bedrock-runtime')

# Define the model ID
model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'

message_list = []

initial_message = {
    "role": "user",
    "content": [
        { "text": "Summarise the the text and provide the top three to five main talking points. Ignore any comments that use bad language, or profanities" },
        { "document": {
            "format":"txt",
            "name":"comments",
            "source":{"bytes":file_contents}
        }} 
    ],
}

message_list.append(initial_message)

response = bedrock.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=message_list,
    inferenceConfig={
        "maxTokens": 4000,
        "temperature": 0
    },
)

response_message = response['output']['message']
print(json.dumps(response_message['content'][0]['text'], indent=4))
