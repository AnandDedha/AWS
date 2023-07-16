import json
import boto3

def lambda_handler(event, context):
    s3_bucket = 'my-json-bucket'
    json_file_name = 'data.json'
    dynamodb_table = 'MyTable'
    
    s3_client = boto3.client('s3')
    dynamodb_client = boto3.client('dynamodb')

    try:
        # Get the JSON object from S3
        response = s3_client.get_object(Bucket=s3_bucket, Key=json_file_name)
        json_data = json.loads(response['Body'].read().decode('utf-8'))
        
        # Insert the JSON data into DynamoDB
        with dynamodb_client.batch_writer(TableName=dynamodb_table) as batch:
            for item in json_data:
                batch.put_item(Item=item)
                
        return {
            'statusCode': 200,
            'body': 'Data successfully loaded into DynamoDB.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
