from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from flask import Flask, request



# Instantiate a new Twilio client object with your account SID and auth token

account_sid = "ACCOUNT_SID"
auth_token = "MY_AUTH_TOKEN"
client = Client(account_sid, auth_token)



# Create a function to handle incoming message

def handle_message(message):
    response = MessagingResponse()
    response.message = "This is a test message from my whatsapp bot!!"
    return str(response)


app = Flask(__name__)


# Use the Twilio client object to create a new webhook and pass in the handle_message function:

@app.route('/ webhook', methods=['POST'])
def webhook():
    message = request.form.get('Body')
    return handle_message(message)


if __name__ == '__main__':
    app.run()
