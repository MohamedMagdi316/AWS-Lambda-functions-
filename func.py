import json
import boto3
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    tableTemperatures = dynamodb.Table('Atmosfera')
    response = tableTemperatures.scan()
    return {
        'statusCode': 200,
        'body': response['Items'][0]['temperatura']
    }

import json
import boto3
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    tableTemperatures = dynamodb.Table('Atmosfera')
    response = tableTemperatures.scan()
    return {
        'statusCode': 200,
        'body': response['Items'][0]['humidade']
    }
