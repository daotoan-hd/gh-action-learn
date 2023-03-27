import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    print(os.environ)
    who_to_greet = os.environ['INPUT_WHO-TO-GREET']
    

if __name__ == '__main__':
    run()
