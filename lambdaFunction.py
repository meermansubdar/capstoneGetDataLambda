import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CapstoneDynamoDBTable')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    vehicle_id = event.get('queryStringParameters', {}).get('vehicleId')
    
    if vehicle_id:
        response = table.query(
            KeyConditionExpression=Key('vehicleId').eq(vehicle_id)
        )
        items = response.get('Items', [])
    else:
        response = table.scan()
        items = response.get('Items', [])
    
    return {
        'statusCode': 200,
        'body': json.dumps(items, cls=DecimalEncoder)
    }


