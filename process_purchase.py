def lambda_handler(event, context):
    print('event:', event)
    response = {
        'TransactionType': event['TransactionType'],
        'Message': 'From Process Purchase',
    }
    return response