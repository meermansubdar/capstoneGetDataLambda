import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    vehicle_id = event.get('vehicleId')
    
    if vehicle_id:
        # Query for specific vehicleId
        data = client.query(
            TableName='CapstoneDynamoDBTable',
            KeyConditionExpression='vehicleId = :vId',
            ExpressionAttributeValues={
                ':vId': {'S': vehicle_id}
            }
        )
    else:
        # Scan entire table if no vehicleId is provided
        data = client.scan(
            TableName='CapstoneDynamoDBTable'
        )
    
    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    
    return response

