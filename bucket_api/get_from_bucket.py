import os

from config import AWS_ACCESS_ID_KEY, AWS_SECRET_ACCESS_KEY

def get(BUCKET_NAME, FILE_NAME, PATH):
    os.system(f'sh get_from_bucket.sh {AWS_ACCESS_ID_KEY} {AWS_SECRET_ACCESS_KEY} {BUCKET_NAME} {FILE_NAME} {PATH}')
