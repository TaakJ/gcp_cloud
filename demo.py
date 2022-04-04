import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tribal-datum-340202-72366d0a0684.json'

storage_client = storage.Client()

"""
Create a New Bucket
"""
#bucket_name = 'tak_data_bucket'
#bucket = storage_client.bucket(bucket_name)
#bucket.location = 'US'
# bucket = storage_client.create_bucket(bucket)

"""
Print Bucket Detail
"""
#vars(bucket)


"""
Accessing a Specifile Bucket
"""
my_bucket = storage_client.get_bucket('tak_data_bucket')


"""
Upload file
"""
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

# file_path = r'D:\Document\Coding\Project\gcp_cloud\datafile'
# upload_to_bucket('picture/dog1', os.path.join(file_path, 'dog.jpg'), 'tak_data_bucket')
# upload_to_bucket('picture/dog2', os.path.join(file_path, 'dog2.jpg'), 'tak_data_bucket')
# upload_to_bucket('picture/dog3', os.path.join(file_path, 'dog3.jpg'), 'tak_data_bucket')
"""
Download file
"""