#!/usr/bin/env python

import re
import sys
import os
from threading import Thread
import datetime
from google.cloud import storage


class storage_config(Thread):

    def __init__(self,project_id, access_id):
        Thread.__init__(self)

        self.project_id = project_id
        self.access_id = access_id

        # path of service account

        file_path = f'D:\Document\Coding\Project\gcp_cloud'
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(file_path, 'tribal-datum-340202-5cd28f25d66f.json')

    def run(self):
        self.bucket_name = 'tasks_bucket'
        self.blob_name1 = 'test1.txt'
        self.blob_name2 = 'test2.txt'
        self.blob_name3 = 'test3.txt'
        self.user_email = 'tak.csithai@gmail.com'
        
        ###############
        ## function ###
        ###############
        
        # hmac_key = self.activate_key(self.access_id, self.project_id)
        self.create_bucket(self.bucket_name)
        # self.delete_bucket(self.bucket_name)
        # self.write_read(self.bucket_name, self.blob_name2)
        # self.compose_file(self.bucket_name, self.blob_name1, self.blob_name2, self.blob_name3)
        # self.delete_blob(self.bucket_name, self.blob_name3)
        # self.generate_signed_url(self.bucket_name, self.blob_name)
        # self.generate_download_signed_url_v4(self.bucket_name, self.blob_name3)
        # self.add_blob_owner(self.bucket_name, self.blob_name3, self.user_email)
        
    def activate_key(self, access_id, project_id):

        storage_client = storage.Client(project=project_id)
        hmac_key = storage_client.get_hmac_key_metadata(
            access_id, project_id=project_id
        )

        print("The HMAC key metadata is:")
        print("Service Account Email: {}".format(hmac_key.service_account_email))
        print("Key ID: {}".format(hmac_key.id))
        print("Access ID: {}".format(hmac_key.access_id))
        print("Project ID: {}".format(hmac_key.project))
        print("State: {}".format(hmac_key.state))
        print("Created At: {}".format(hmac_key.time_created))
        print("Updated At: {}".format(hmac_key.updated))
    
        return hmac_key
    
    def create_bucket(self, bucket_name):
        
        storage_client = storage.Client()
        bucket = storage_client.create_bucket(bucket_name)

        print("Bucket {} created".format(bucket.name))
        
    def write_read(self, bucket_name, blob_name):
        """Write and read a blob from GCS using file-like IO"""
        
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        with blob.open("w") as f:
            # f.write("Hello World !!")
            f.write("My name is Thanakit Jitcharoenjai")

        with blob.open("r") as f:
            print(f.read())
            
    def generate_signed_url(self, bucket_name, blob_name):
        
        # bucket_name = 'your-bucket-name'
        # blob_name = 'your-object-name'

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        url = blob.generate_signed_url(
            # This URL is valid for 1 hour
            expiration=datetime.timedelta(minutes=10),
            # Allow GET requests using this URL.
            method="GET",
        )

        print("The signed url for {} is {}".format(blob.name, url))
        return url
    
    def generate_download_signed_url_v4(self, bucket_name, blob_name):
        
        # bucket_name = 'your-bucket-name'
        # blob_name = 'your-object-name'

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        url = blob.generate_signed_url(
            version="v4",
            # This URL is valid for 15 minutes
            expiration=datetime.timedelta(minutes=15),
            # Allow GET requests using this URL.
            method="GET",
        )

        print("Generated GET signed URL:")
        print(url)
        print("You can use this URL with any user agent, for example:")
        print("curl '{}'".format(url))
        return url
    
    def compose_file(self, bucket_name, first_blob_name, second_blob_name, destination_blob_name):
        
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        destination = bucket.blob(destination_blob_name)
        destination.content_type = "text/plain"

        # sources is a list of Blob instances, up to the max of 32 instances per request
        sources = [bucket.get_blob(first_blob_name), bucket.get_blob(second_blob_name)]
        destination.compose(sources)

        print(
            "New composite object {} in the bucket {} was created by combining {} and {}".format(
                destination_blob_name, bucket_name, first_blob_name, second_blob_name
            )
        )
        return destination
    
    def add_blob_owner(self, bucket_name, blob_name, user_email):

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.acl.reload()
        blob.acl.user(user_email).grant_owner()
        blob.acl.save()

        print(
            "Added user {} as an owner on blob {} in bucket {}.".format(
                user_email, blob_name, bucket_name
            )
        )
        
    def delete_blob(self, bucket_name, blob_name):

        storage_client = storage.Client()

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()

        print("Blob {} deleted.".format(blob_name))
        
        
    def delete_bucket(self, bucket_name):

        storage_client = storage.Client()

        bucket = storage_client.get_bucket(bucket_name)
        bucket.delete()

        print("Bucket {} deleted".format(bucket.name))


if __name__ == "__main__":
    
    # setting service account
    project_id = 'tribal-datum-340202'
    access_id = 'GOOG1E6OD2KC4PDZE3KHCJMSJAN5ZHJXVJ6FKUSXOVAUDLFNBTVGFLUCABKPA'

    gen = storage_config(project_id, access_id)
    gen.start()
    gen.join()