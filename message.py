from twilio.rest import Client 
 
account_sid = 'AC5e7d9b0bdf266ba786913630b8a0d8d4' 
auth_token = 'b35b50f47561d5dbf4f690cacb0f6ee1' 
client = Client(account_sid, auth_token) 

def automate_message():  
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Good Morning Rahul... Please take glass of warm water',      
                                to='whatsapp:+916205192178' 
                            ) 
    
    print(message.sid)