import json
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Extract data from the event
    data = event['data']
    
    # Transform the data
    transformed_data = transform_data(data)
    
    # Log success
    logger.info("Data transformation successful.")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data transformation successful')
    }

def transform_data(data):
    # Example: Perform transformations on the data
    transformed_data = {}
    for key, value in data.items():
        if key == 'product_id':
            transformed_data[key] = int(value)
        elif key == 'category':
            transformed_data[key] = value.upper()
        else:
            transformed_data[key] = value
    return transformed_data
