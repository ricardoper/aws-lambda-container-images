import json
from datetime import datetime

def lambda_handler(event, context):
    now: str = datetime.now().strftime('%Y/%m/%d %H:%M:%S ')

    print(now + ' * DEBUG: Hello world!')
    print(now + ' * EVENT: ' + str(event))

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
