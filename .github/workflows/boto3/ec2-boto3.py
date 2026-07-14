import boto3
from dotenv import load_dotenv
import os

load_dotenv()

session = boto3.Session(
aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
region_name=os.getenv('AWS_REGION')
)

ec2 = session.client("ec2")

response = ec2.run_instances(
    ImageId="ami-01a00762f46d584a1",   # replace with valid AMI ID
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

print(response)
