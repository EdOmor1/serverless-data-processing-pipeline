import boto3
import json
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Extract data from the event
    data = event['data']
    
    # Process the data (e.g., validate, clean, format)
    processed_data = process_data(data)
    
    # Store the processed data in RDS
    store_in_rds(processed_data)
    
    # Log success
    logger.info("Data ingestion successful.")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data ingestion successful')
    }

def process_data(data):
    # Example: Validate and clean data
    processed_data = {}
    for key, value in data.items():
        if key == 'timestamp':
            processed_data[key] = value
        elif key == 'user_id':
            processed_data[key] = int(value)
        elif key == 'purchase_amount':
            processed_data[key] = float(value)
        else:
            processed_data[key] = value
    return processed_data

def store_in_rds(data):
    # Example: Store data in RDS
    rds_client = boto3.client('rds')
    # Code to connect and store data in RDS
    pass
