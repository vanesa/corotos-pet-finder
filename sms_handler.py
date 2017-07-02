from flask import Flask, request
try:
    import secrets
import redis

twillio_account_sid = secrets.TWILIO_ACCOUNT_SID
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

@app.route('/sms', method=['POST'])
def handle_sms():
	user = request.form['From']
	pet = request.form['Body'].strip().lower()

	redis_client.sadd(pet, user.encode('utf-8'))

if __name__ == '__main__':
	app.run(debug=True)
