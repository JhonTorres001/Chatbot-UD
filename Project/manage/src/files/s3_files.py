import boto3


def upload_file(fileName, content):

    s3 = boto3.resource('s3')
    object = s3.Object('rasa-api-bucker', fileName)
    object.put(Body=content)
