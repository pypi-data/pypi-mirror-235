"""Console script for wasabi S3."""
import sys
import click
import threading
import boto3
from time import sleep
import botocore.config
from botocore.exceptions import EndpointConnectionError


class indicators:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    OKMAGENTA = "\033[35m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class WasabiPurge:
    def __init__(self, ACCESS_KEY_ID, SECRET_ACCESS_KEY, ENDPOINT, BUCKET_NAME, PREFIX=''):
        self.accessKey = ACCESS_KEY_ID
        self.secretAccessKey = SECRET_ACCESS_KEY
        self.endPoint = ENDPOINT
        self.bucketName = BUCKET_NAME
        self.prefix = PREFIX

        self.config = botocore.config.Config(
            retries=dict(max_attempts=10),
            connect_timeout=120,
            read_timeout=120,
            max_pool_connections=90,
        )

        self.S3Resource = boto3.resource(
            "s3",
            endpoint_url=self.endPoint,
            aws_access_key_id=self.accessKey,
            aws_secret_access_key=self.secretAccessKey,
            config=self.config,
        )

        self.S3Client = boto3.client(
            "s3",
            endpoint_url=self.endPoint,
            aws_access_key_id=self.accessKey,
            aws_secret_access_key=self.secretAccessKey,
            config=self.config,
        )

        self.bucket = self.S3Resource.Bucket(self.bucketName)

        self.params = dict()

        if len(self.prefix) > 0:
            self.params = {'Bucket': self.bucketName, 'Prefix': self.prefix}
        else:
            self.params = {'Bucket': self.bucketName}


    def deleteNonCurrentsOnly(self, bucket_name, prefix, objects_to_delete, thread_id, batch_size, max_retries=3):
        # bucket_name, prefix, objects_to_delete, thread_id, batch_size, max_retries = 3

        paginator = self.S3Client.get_paginator("list_object_versions")
        batch_counter = 1
        # for page in paginator.paginate(Bucket=self.bucketName, Prefix=self.prefix):
        for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
            for version in page.get("Versions", []):
                if not version['IsLatest']:
                    objects_to_delete.append({'Key': version['Key'], 'VersionId': version['VersionId']})

                if len(objects_to_delete) >= batch_size:
                    try:
                        response = self.S3Client.delete_objects(
                            Bucket=self.bucketName,
                            Delete={"Objects": objects_to_delete, "Quiet": False},
                        )

                        for i in range(len(objects_to_delete)):
                            print(
                                f"\r|-- Batch Number [{batch_counter}]: {i + 1} out of {len(objects_to_delete)} deleted --|",
                                end="",
                            )
                            sleep(0.001)

                        batch_counter += 1

                        objects_to_delete.clear()
                    except EndpointConnectionError:
                        print(
                            f"Thread {thread_id}: Network error during batch delete"
                        )

        if objects_to_delete:
            try:
                response = self.S3Client.delete_objects(
                    Bucket=self.bucketName,
                    Delete={"Objects": objects_to_delete, "Quiet": False},
                )
                for i in range(len(objects_to_delete)):
                    print(
                        f"\r|-- Batch Number [{batch_counter}]: {i + 1} out of {len(objects_to_delete)} deleted --|",
                        end="",
                    )
                    sleep(0.001)

            except EndpointConnectionError:
                print(
                    f"Thread {thread_id}: Network error during object deletion"
                )


    def NonCurrentsDeleteMultithreadedProcessor(self, bucket_name, prefix, batch_size=1000, num_threads=5):
        threads = []
        objects_to_delete = [[] for _ in range(num_threads)]

        for i in range(num_threads):
            thread = threading.Thread(
                target=self.deleteNonCurrentsOnly,
                # args=(self.bucketName, self.prefix, objects_to_delete[i], i, self.batch_size),
                args=(bucket_name, prefix, objects_to_delete[i], i, batch_size)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


    def deleteAllObjects(self,  bucket_name, prefix, objects_to_delete, thread_id, batch_size, max_retries=10):
        # objects_to_delete = list()
        paginator = self.S3Client.get_paginator("list_object_versions")
        batch_counter = 1
        # for page in paginator.paginate(Bucket=self.bucketName, Prefix=self.prefix):
        for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
            for version in page.get("Versions", []):
                objects_to_delete.append(
                    {"Key": version["Key"], "VersionId": version["VersionId"]}
                )

                # batch_counter = 1
                if len(objects_to_delete) >= batch_size:
                    try:
                        response = self.S3Client.delete_objects(
                            Bucket=self.bucketName,
                            Delete={"Objects": objects_to_delete, "Quiet": False},
                        )

                        for i in range(len(objects_to_delete)):
                            print(
                                f"\r|-- Batch Number [{batch_counter}]: {i + 1} out of {len(objects_to_delete)} deleted --|",
                                end="",
                            )
                            sleep(0.001)

                        batch_counter += 1

                        objects_to_delete.clear()
                    except EndpointConnectionError:
                        print(
                            f"Thread {thread_id}: Network error during batch delete"
                        )

        if objects_to_delete:
            try:
                response = self.S3Client.delete_objects(
                    Bucket=self.bucketName,
                    Delete={"Objects": objects_to_delete, "Quiet": False},
                )
                for i in range(len(objects_to_delete)):
                    print(
                        f"\r|-- Batch Number [{batch_counter}]: {i + 1} out of {len(objects_to_delete)} deleted --|",
                        end="",
                    )
                    sleep(0.001)

            except EndpointConnectionError:
                print(
                    f"Thread {thread_id}: Network error during object deletion"
                )


    def FullDeleteMultithreadedProcessor(self, bucket_name, prefix, batch_size=1000, num_threads=5):
        threads = []
        objects_to_delete = [[] for _ in range(num_threads)]

        for i in range(num_threads):
            thread = threading.Thread(
                target=self.deleteAllObjects,
                # args=(self.bucketName, self.prefix, objects_to_delete[i], i, self.batch_size),
                args=(bucket_name, prefix, objects_to_delete[i], i, batch_size)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


    def deleteAllObjectsInBucketController(self):
        self.FullDeleteMultithreadedProcessor(self.bucketName, self.prefix)

    def deleteNonCurrentsObjectsInBucketController(self):
        self.NonCurrentsDeleteMultithreadedProcessor(self.bucketName, self.prefix)


    def purgeDeleteMarkers(self):
        print(
            f"{indicators.HEADER}You have chosen to purge all delete markers (DMs)!{indicators.ENDC}"
        )
        bucket_name = self.bucketName

        # Paginate through all the delete markers in the bucket
        delete_markers = []

        paginator = self.S3Resource.meta.client.get_paginator("list_object_versions")
        for page in paginator.paginate(**self.params):
            for version in page.get("Versions", []):
                if version.get("IsDeleteMarker"):
                    delete_markers.append(
                        {
                            "VersionId": version.get("VersionId"),
                            "Key": version.get("Key"),
                        }
                    )

                    # Delete a batch of 50000 delete markers
                    if len(delete_markers) == 50000:
                        for delete_marker in delete_markers:
                            self.S3Client.delete_object(
                                Bucket=bucket_name,
                                Key=delete_marker["Key"],
                                VersionId=delete_marker["VersionId"],
                            )
                        delete_markers = []

        # Delete any remaining delete markers
        for delete_marker in delete_markers:
            self.S3Resource.delete_object(
                Bucket=bucket_name,
                Key=delete_marker["Key"],
                VersionId=delete_marker["VersionId"],
            )

        print(
            f"{indicators.OKBLUE}Delete Markets Successfully Purged from {self.bucketName}{indicators.OKBLUE}"
        )


    def deleteBucket(self):

        self.deleteAllObjectsInBucketController()
        self.purgeDeleteMarkers()

        bucket = self.S3Resource.Bucket(self.bucketName)

        # Ensure nothing else remains
        bucket.objects.all().delete()

        # Delete the bucket
        bucket.delete()

        print(f"Bucket deletion successful!")




def initialize():
    accessKey = input(
        f"{indicators.OKCYAN}Enter your Access Key ID: {indicators.ENDC}"
    ).strip()
    secretAccessKey = input(
        f"{indicators.OKCYAN}Enter your Secret Access Key: {indicators.ENDC}"
    ).strip()
    bucketName = input(
        f"{indicators.OKCYAN}Enter your Bucket Name: {indicators.ENDC}"
    ).strip()
    endpoint = input(
        f"{indicators.OKCYAN}Specify the endpoint URL: {indicators.ENDC}"
    ).strip()

    prefix = input(
        f"{indicators.OKCYAN}Enter to continue or Specify a Prefix): {indicators.ENDC}"
    ).strip()

    WasabiClient = WasabiPurge(accessKey, secretAccessKey, endpoint, bucketName, prefix)

    return WasabiClient


class ScriptRunner:
    def __init__(self):
        pass

    def startMessage(self):
        for i in range(3):
            print(
                f"\rPlease wait. Script is starting{'.' * i}\n",
                end="",
            )
            sleep(0.01)


    def start(self):

        WasabiClient = initialize()

        print(
            f"{indicators.OKGREEN}Choose from the following list of operations to run on your Wasabi bucket: {WasabiClient.bucketName}"
        )
        print(
            f"\t{indicators.OKMAGENTA}Operation 1: Delete Non-Current Objects {indicators.ENDC}"
        )
        print(
            f"\t{indicators.OKMAGENTA}Operation 2: Delete Current and Non-Current Objects {indicators.ENDC}"
        )
        print(
            f"\t{indicators.OKMAGENTA}Operation 3: Purge Delete Markers {indicators.ENDC}"
        )
        print(f"\t{indicators.OKMAGENTA}Operation 4: Delete Bucket {indicators.ENDC}")

        acceptableOptions = [1, 2, 3, 4]
        userSelection = int(
            input(
                f"{indicators.WARNING}Select Operation (Number 1-4) : {indicators.ENDC}"
            ).strip()
        )

        if userSelection not in acceptableOptions:
            print(
                f"{indicators.FAIL}Wrong Option Selected :( Try again!{indicators.ENDC}"
            )
        else:
            if userSelection == 1:
                self.startMessage()
                WasabiClient.deleteNonCurrentsObjectsInBucketController()
            elif userSelection == 2:
                self.startMessage()
                WasabiClient.deleteAllObjectsInBucketController()
            elif userSelection == 3:
                self.startMessage()
                WasabiClient.purgeDeleteMarkers()
            elif userSelection == 4:
                self.startMessage()
                WasabiClient.deleteBucket()


@click.command()
def main(args=None):
    """Console script for wasabi S3."""
    click.echo(
        f"{indicators.WARNING}Welcome to the Wasabi S3 CLI Tool{indicators.ENDC}"
    )
    click.echo(
        f"{indicators.WARNING}--------------------------------------------------------{indicators.ENDC}"
    )
    click.echo(f"{indicators.OKCYAN}@author: Salim Dason{indicators.ENDC}")
    click.echo(f"{indicators.OKCYAN}@version: 17 October 2023 Update{indicators.ENDC}")
    click.echo(
        f"{indicators.OKCYAN}@licence: GNU GENERAL PUBLIC LICENSE{indicators.ENDC}"
    )
    click.echo(
        f"{indicators.FAIL}Note: Tool specifically designed for versioned buckets!{indicators.ENDC}"
    )
    click.echo(
        f"{indicators.WARNING}---------------------------------------------------------{indicators.ENDC}\n"
    )

    ScriptRunner().start()


if __name__ == "__main__":
    # main()
    sys.exit(main())
