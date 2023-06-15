import json
from email_handler import *
from read_rule import *
from get_global_variables import *

def lambda_handler(event, context):
    
    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                handle_insert(record)
    except Exception as e:
        print(e)
        
def handle_insert(record):
    newImage = record['dynamodb']['NewImage']
    email = newImage['email']['S']
    subject = newImage['subject']['S']
    body = newImage['body']['S']
    order_value = newImage['order_value']['N']
    order_value_type = newImage['order_value_type']['S']
    customer_name = newImage['customer_name']['S']
    order_id = newImage['order_id']['S']
    to_address = newImage['email']['S']
    
    premium_item = get_premium_rule('premium')
    send_notification = premium_item['send_notification']
    min_transaction_value = premium_item['min_transaction_value']
    max_transaction_value = premium_item['max_transaction_value']
    unit = premium_item['unit']
    
    
    if ((int(order_value) >= int(min_transaction_value)) and (int(order_value) <= int(max_transaction_value))):
        subject = " High value transaction"
        body_text = "Transaction details : "
        body_html = "Customer " + customer_name  + " has created an order of value " +  order_value + unit+ ".Please check Order " + order_id +" for details"
        send_email_status = sendEmail(region,sender,to_address,application_id,subject,body_text,body_html,charset)
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    else:
        print("inside else part")
    return
        
