import logging
import boto3
from botocore.exceptions import ClientError


client=boto3.client('s3')


def input_bucket_from_user():
    bucket_name = str(input("Enter bucket name= "))
    region = str(input("Enter Region name= "))
    return bucket_name,region

# Create bucket

def create_bucket(bucket_name, region):
    location = {'LocationConstraint': region}
    client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)
    print("Bucket Created")

# List all buckets

def list_buckets():
    clientResponse = client.list_buckets()
    print('Printing bucket names...')
    for bucket in clientResponse['Buckets']:
        print(f'Bucket Name: {bucket["Name"]}')


# List buckets from specific region

def list_buckets_from_specific_region():
    clientResponse = client.list_buckets()
    region_buckets = [bucket["Name"] for bucket in client.list_buckets()["Buckets"] if client.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint'] == 'ap-south-1']
    print("list of bucket",region_buckets)

# - Delete bucket

def delete_bucket():
     s3 = boto3.resource('s3')
     my_bucket = s3.Bucket('rathanademo').delete()
     print('Bucket has been deleted')

# - upload file to bucket
def upload_file():
    s3 = boto3.client('s3')
    with open("index.html", "rb") as f:
        s3.upload_fileobj(f, "rathanademo", "index.html")

# List file in bucket

def list_file():
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('rathanademo')
    for file in my_bucket.objects.all():
        print(file.key)

# - download file

def download_file():
    s3 = boto3.client('s3')
    with open('index.html', 'wb') as f:
        s3.download_fileobj('rathanademo', 'index.html', f)
    print("File Downloaded")

# - delete file


if __name__ == "__main__":
    check = True
    while(check):
        choice = int(input("----------------------------------------\nEnter Choice:\n1. Create bucket\n2. List All Bucket\n3. List buckets from specific region\n4. Upload file to bucket\n5. List file uploaded in bucket\n6. Download File from Bucket\n7. Delete file\n8. Delete Bucket\n9. Quit \n----------------------------------------\nEnter choice : "))
        if(choice==1):
            # select = int(input("----------------------------------------\nEnter Choice:\n1. Input detail\n2. Quit \n----------------------------------------\nEnter choice : "))
            # if (select==1):
                # input_bucket_from_user()
            create_bucket('rathanademo','ap-south-1')
        elif(choice==2):
            list=list_buckets()
            print(list)
        elif(choice==3):
            list_buckets_from_specific_region()
        elif(choice==4):
            upload_file()
        elif(choice==5):
            list_file()
        elif(choice==6):
            download_file()
        elif(choice==7):
           client = boto3.resource('s3')
           bucket = client.Bucket('rathanademo')
           bucket.objects.all().delete()
        elif(choice==8):
            delete_bucket()
        else:
            break;