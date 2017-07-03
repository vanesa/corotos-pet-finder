from flask import Flask, request
try:
    import secrets
import redis
from twilio.twiml.messaging_response import MessagingResponse

twillio_account_sid = secrets.TWILIO_ACCOUNT_SID
my_number = secrets.MY_NUMBER
requested_pets = {'cavalier', 'king charles spaniel'}

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

def respond(user, body):
    response = MessagingResponse()
    response.message(body=body)
    return str(response)

@app.route('/sms', method=['POST'])
def handle_sms():
	user = request.form['From']
	pet = request.form['Body'].strip().lower()
	if pet not in requested_pets:
        return respond(user, body="Hm, that doesn't look like a valid pet. Try something like 'Cavalier'.")
 
    redis_client.sadd(pet, user.encode('utf-8'))
        return respond(user, body=f"Sweet action. We'll let you know when there are {pet}'s available.")


if __name__ == '__main__':
	app.run(debug=True)
