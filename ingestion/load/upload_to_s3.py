import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

BUCKET = os.getenv("S3_BUCKET_NAME")

LOCAL_DATASET = Path("data/raw")


def upload_directory():

    for file in LOCAL_DATASET.glob("*.csv"):

        print(f"Uploading {file.name}...")

        s3.upload_file(
            str(file),
            BUCKET,
            f"raw/{file.name}"
        )

    print("Upload Completed")


if __name__ == "__main__":
    upload_directory()