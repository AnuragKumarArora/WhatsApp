from twilio.rest import Client
import schedule
import time

def whatsAppMessageJob(message):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body=message,
                                  to='whatsapp:+91xxxxxxxxxx'
                              )
    print(message.sid)

schedule.every().hour.do(whatsAppMessageJob,"Message sample")
while True:
    schedule.run_pending()
    time.sleep(1)