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
	target_pet = request.form['Body'].strip().lower()
	
	if target_pet not in requested_pets:
		return respond(user, body="Hm, that doesn't look like a valid pet. Try something like 'Beagle'.")

	redis_client.sadd('subscribed_pets', target_pet)
	redis_client.sadd(target_pet, user.encode('utf-8'))
	return respond(user, body="Sweet action. We'll let you know when there are " + target_pet.capitalize() + "'s available.")


if __name__ == '__main__':
	app.run(debug=True)
