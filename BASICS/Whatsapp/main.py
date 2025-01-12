# TWilio is a module of python which is used to send messages to the phone number

# Date Time need to send message (Datetime module)
# time module

'''
1- twilio client setup
2- user input 
3-schedule message logic
4- send message 
'''

#step-1
from twilio.rest import Client
from datetime import timedelta , datetime 
import time 

#step - 2 
account_sid = 'AC1aac6ba19c3b363282528fd134e7708f'
auth_token = 'e2f3da589967d95ba0a64078947a6edf'

print(datetime.now())

client = Client(account_sid,auth_token)

#step-3
def send_message(receiver,message):
    try:
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to=f'whatsapp:{receiver}'
        )
        print(f'message successfully sent to {receiver}')
        
    except Exception as e:
        print(f'Error Occured as {e}')

#step-4
name=input('Enter the name of the receiver: ')
receiver=input('Enter the whatsapp number of the receiver with country code (eg: +91): ')
messsage_body=input(f'Enter the message you want to send {name} : ')

#step - 5
date_str = input('Enter the date you want to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time you want to send the message (HH:MM:SS): ')

# step 6 
schedule_date = datetime.strptime(f'{date_str} {time_str}','%Y-%m-%d %H:%M') # Ex - 2024-12-22 17:04:15.855711
current_date = datetime.now()   # Ex - 2024-12-22 17:04:15.855711

# calculate delay 
time_difference = schedule_date - current_date 
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('Invalid date and time')
else:
    print(f'Message  to be sent to {name} on {date_str} at {time_str}')
    time.sleep(delay_seconds)
    send_message(receiver,messsage_body)

