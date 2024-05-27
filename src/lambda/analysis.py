import json
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Extract data from the event
    data = event['data']
    
    # Analyze the data
    analysis_result = analyze_data(data)
    
    # Log success
    logger.info("Data analysis successful.")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data analysis successful')
    }

def analyze_data(data):
    # Example: Perform analysis on the data
    analysis_result = {}
    analysis_result['total_visits'] = len(data['visits'])
    analysis_result['total_purchases'] = len(data['purchases'])
    # Additional analysis logic...
    return analysis_result
