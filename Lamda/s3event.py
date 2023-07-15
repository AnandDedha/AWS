import boto3

def lambda_handler(event, context):
    # Retrieve the S3 bucket and object information from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    print(bucket_name)
    print(object_key)
    
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    # Retrieve the uploaded file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    file_content = response['Body'].read().decode('utf-8')
    
    # Perform some processing or business logic with the file content
    # For example, you could process the data, extract information, or store it in a database.
    # Here, we'll simply print the file content for demonstration purposes.
    print(file_content)
    
    # Return a response if needed
    return {
        'statusCode': 200,
        'body': 'File uploaded and processed successfully.'
    }
