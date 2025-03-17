import os

from config import AWS_ACCESS_ID_KEY, AWS_SECRET_ACCESS_KEY

def upload(BUCKET_NAME, PATH_TO_FILE):
    os.system(f'sh upload_to_bucket.sh {AWS_ACCESS_ID_KEY} {AWS_SECRET_ACCESS_KEY} {BUCKET_NAME} {PATH_TO_FILE}')
