import boto3
from tqdm import tqdm
import logging
import os

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the desired logging level (DEBUG for more verbose logging)
logging.basicConfig(level=logging.INFO)



session = boto3.Session(region_name='us-east-1')
boto3.set_stream_logger('', logging.INFO)
client = boto3.client("bedrock-runtime")

messages = [{"role": "user", "content": [{"text": "What is your name?"}]}]

response = client.converse(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=messages,
)
#anthropic.claude-3-sonnet-20240229-v1:0
print(response)