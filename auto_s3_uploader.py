from secrests import secret_access_key,access_key
import concurrent.futures
import boto3
import os
import time

client=boto3.client('s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_access_key)


t1=time.perf_counter()

def file_uploader(file):
    if '.py' in file:
        upload_file_bucket='lambda-s3-test-python'
        upload_file_key='python/'+str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)

    if '.docx' in file:
        upload_file_bucket='lambda-s3-test-python'
        upload_file_key='Docs/'+str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)

    if '.pdf' in file:
        upload_file_bucket='lambda-s3-test-python'
        upload_file_key='pdf/'+str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)

    if '.xlsx' in file:
        upload_file_bucket='lambda-s3-test-python'
        upload_file_key='Excel/'+str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)

    if '.jpg' in file:
        upload_file_bucket='lambda-s3-test-python'
        upload_file_key='Images/'+str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)

    if '.png' in file:
        upload_file_bucket='lambda-s3-test-python'
        upload_file_key='Screenshots/'+str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)
file=os.listdir()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(file_uploader,file)

t2=time.perf_counter()

print("Total Time Taken",t2-t1)