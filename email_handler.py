import boto3
from botocore.exceptions import ClientError
def sendEmail(aws_region,sender,to_address,app_id,subject,body_text,body_html,charset):
            
    # Create a new client and specify a region.
    client = boto3.client('pinpoint',region_name=aws_region)
    try:
        response = client.send_messages(
            ApplicationId=app_id,
            MessageRequest={
                'Addresses': {
                    to_address: {
                         'ChannelType': 'EMAIL'
                    }
                },
                'MessageConfiguration': {
                    'EmailMessage': {
                        'FromAddress': sender,
                        'SimpleEmail': {
                            'Subject': {
                                'Charset': charset,
                                'Data': subject
                            },
                            'HtmlPart': {
                                'Charset': charset,
                                'Data': body_html
                            },
                            'TextPart': {
                                'Charset': charset,
                                'Data': body_text
                            }
                        }
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return("Error")
    else:
        print( response['MessageResponse'])
        return("Success")