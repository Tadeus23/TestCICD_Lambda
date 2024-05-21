import json
from src.extra_utils import get_lambda_message

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(get_lambda_message())
    }

if __name__ == '__main__':
    print(lambda_handler({}, {}))