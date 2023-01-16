import json

def lambda_handler(event, context):
    statusCode: int = 200
    bodyResponse: dict = {
        'msg': 'Hello world!'
    }

    print(' * DEBUG: Hello world!')
    print(' * EVENT: ' + str(event))

    return {
        'statusCode': statusCode,
        'body': json.dumps(bodyResponse | event)
    }
