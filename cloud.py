import json

def lambda_handler(event, context):
    # Extract IoT message from the Lambda event
    iot_message = json.loads(event['body'])

    # Process the IoT data (replace this with your processing logic)
    processed_data = process_iot_data(iot_message)

    # Return a response (e.g., for debugging purposes)
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Processing successful", "data": processed_data})
    }

    return response

def process_iot_data(iot_data):
    # Implement your custom IoT data processing logic here
    # This is a placeholder, replace it with your actual processing code
    processed_data = {
        "original_data": iot_data,
        "processed_result": "Your processing logic here"
    }
    return processed_data
