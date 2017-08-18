from flask import Flask, request
import redis
from secrets import twilio_account_sid, token, my_number
from twilio.twiml.messaging_response import MessagingResponse

# Dog breeds from https://dog.ceo/api/breeds/list
dog_breeds = {"affenpinscher", "african", "airedale", "akita", "appenzeller", "basenji", "beagle",
"bluetick", "borzoi", "bouvier", "boxer", "brabancon", "briard", "bulldog", "bullterrier", "cairn",
"chihuahua", "chow", "clumber", "collie", "coonhound", "corgi", "dachshund", "dane", "deerhound",
"dhole", "dingo", "doberman", "elkhound", "entlebucher", "eskimo", "germanshepherd", "greyhound", "groenendael",
"hound", "husky", "keeshond", "kelpie", "komondor", "kuvasz", "labrador", "leonberg", "lhasa", "malamute", "malinois",
"maltese", "mastiff", "mexicanhairless", "mountain", "newfoundland", "otterhound", "papillon", "pekinese",
"pembroke", "pinscher", "pointer", "pomeranian", "poodle", "pug", "pyrenees", "redbone", "retriever", "ridgeback",
"rottweiler", "saluki","samoyed", "schipperke", "schnauzer", "setter", "sheepdog", "shiba", "shihtzu", "spaniel",
"springer", "stbernard", "terrier", "vizsla", "weimaraner", "whippet", "wolfhound"}


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
	target_dog = request.form['Body'].strip().lower()
	
	if target_dog not in dog_breeds:
		return respond(user, body="Hm, that doesn't look like a valid dog breed. Try something like 'Beagle'.")

	redis_client.sadd('subscribed_dogs', target_dog)
	redis_client.sadd(target_dog, user.encode('utf-8'))
	return respond(user, body="Sweet action. We'll let you know when there are " + target_dog.capitalize() + "'s available.")


if __name__ == '__main__':
	app.run(debug=True)
