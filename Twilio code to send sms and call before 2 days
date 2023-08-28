from twilio.rest import Client
from datetime import datetime, timedelta

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

# Borrower's phone number
borrower_phone_number = '+1234567890'

# Calculate the reminder date (2 days before repayment date)
repayment_date = datetime.now() + timedelta(days=7)  # Example: Repayment due in 7 days
reminder_date = repayment_date - timedelta(days=2)

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send SMS reminder
sms_message = client.messages.create(
    body='Your loan repayment is due on {}. Please make sure to repay on time.'.format(repayment_date.date()),
    from_=twilio_phone_number,
    to=borrower_phone_number
)
print('SMS reminder sent with SID:', sms_message.sid)

# Make call reminder
call = client.calls.create(
    twiml='<Response><Say>Your loan repayment is due on {}. Please make sure to repay on time.</Say></Response>'.format(repayment_date.date()),
    from_=twilio_phone_number,
    to=borrower_phone_number
)
print('Call reminder initiated with SID:', call.sid)
