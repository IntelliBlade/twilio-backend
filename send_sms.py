import sys
import os
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError
from twilio.rest import Client

load_dotenv()

# OpenAI setup
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Prompt to send to OpenAI (will be sourced from elsewhere later)
prompt = "Say hello world"

try:
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    ai_message = response.choices[0].message.content
except AuthenticationError:
    print("Error: Invalid OpenAI API key. Check your OPENAI_API_KEY in .env")
    #sys.exit(1)
except APIConnectionError:
    print("Error: Could not connect to OpenAI. The service may be down.")
    #sys.exit(1)
ai_message = "This is a test message from Twilio" ##REMOVE THIS LINE TO USE OPENAI and uncomment the lines quitting if openai fails.
print("OpenAI response:", ai_message)

# Twilio setup
twilio_client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

msg = twilio_client.messages.create(
    from_=os.environ["TWILIO_FROM_NUMBER"],
    to=os.environ["TO_NUMBER"],
    body=ai_message,
)

print("Sent:", msg.sid)
