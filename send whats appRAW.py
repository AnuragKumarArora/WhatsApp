from twilio.rest import Client

import schedule
import time

def job():
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='this is anurag. pls ping me !',
                                  to='whatsapp:+9181XXXXXXXX'
                              )

    print(message.sid)

schedule.every().hour.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
