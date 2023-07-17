import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    print(s3_bucket)
    print(json_file_name)
    
    
    s3_client = boto3.client('s3')
    dynamodb_client = boto3.resource('dynamodb')
    dynamodb_table = dynamodb_client.Table('Carplatenumberinfo')

    try:
        # Get the JSON object from S3
        response = s3_client.get_object(Bucket=s3_bucket, Key=json_file_name)
        json_data = json.loads(response['Body'].read().decode('utf-8'), parse_float=Decimal)
        
        # Insert the JSON data into DynamoDB
        with dynamodb_table.batch_writer() as batch:
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
        





import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    #json_file_name = event['Records'][0]['s3']['object']['key']
    json_file_name ='carsinfo.json'
    print(s3_bucket)
    print(json_file_name)
    
    #dynamodb_table = 'Carplatenumberinfo'
    #print(dynamodb_table)
    
    s3_client = boto3.client('s3')
    print(s3_client)
    dynamodb_client = boto3.resource('dynamodb')
    print(dynamodb_client)
    dynamodb_table = dynamodb_client.Table('Carplatenumberinfo')

    try:
        # Get the JSON object from S3
        print("We are in Try")
        response = s3_client.get_object(Bucket=s3_bucket, Key=json_file_name)
        print(response)
        json_data = json.loads(response['Body'].read().decode('utf-8'), parse_float=Decimal)
        print(json_data)
        
        # Insert the JSON data into DynamoDB
        with dynamodb_table.batch_writer() as batch:
            print("In the batch_writer")
            for item in json_data:
                print(item)
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
        
        
        
       
       
