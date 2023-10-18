import boto3
from ddaptools.aws_classes.class_enhancement import *
from ddaptools.dda_constants import *
import uuid

sqs = boto3.client('sqs')

# Define the URL of your SQS queue
queue_url = 'https://sqs.us-east-1.amazonaws.com/796522278827/ProcessingQueue.fifo'

def test_enqueue_all():
    
    
    message_deduplication_id = str(uuid.uuid4())

    for staging_guid in ["866a6922-d591-40f0-976b-cf6b3c6e2178",
                         "8f56dc18-d693-4ef1-86ce-977a1d0ae2e4"]:
        print("Enqueue: ", staging_guid)
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=staging_guid,
            MessageGroupId=staging_guid,
            MessageDeduplicationId=message_deduplication_id,
        )
        print(response)


