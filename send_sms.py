import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

msg = client.messages.create(
    from_=os.environ["TWILIO_FROM_NUMBER"],
    to=os.environ["TO_NUMBER"],
    body="Hello from Ubuntu + Twilio 🚀",
)

print("Sent:", msg.sid)

