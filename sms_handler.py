from flask import Flask, request
import redis
from secrets import twilio_account_sid, token, my_number
from twilio.twiml.messaging_response import MessagingResponse

requested_pets = {'beagle', 'king charles spaniel', 'cavalier', 'shihtzu'}

app = Flask(__name__)

def respond(user, body):
    response = MessagingResponse()
    response.message(body=body)
    
    return str(response)

@app.route('/sms', methods=['POST'])
def handle_sms():

	redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

	if request.form['AccountSid'] != twilio_account_sid:
		return '', 400

	user = request.form['From']
	pet = request.form['Body'].strip().lower()
	
	if pet not in requested_pets:
		return respond(user, body="Hm, that doesn't look like a valid pet. Try something like 'Johnson'.")

	redis_client.sadd(pet, user.encode('utf-8'))
	return respond(user, body="Sweet action. We'll let you know when there are {pet}'s available.")


if __name__ == '__main__':
	app.run(debug=True)
