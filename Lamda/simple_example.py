def lambda_handler(event, context):
    name = event['name']
    age = event['age']
    
    if age >= 18:
        message = f"Hello, {name}! You are eligible to vote."
    else:
        message = f"Hi, {name}! You are not yet eligible to vote."
    
    return message
