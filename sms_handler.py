from flask import Flask, request
try:
    import secrets

twillio_account_sid = secrets.TWILIO_ACCOUNT_SID

app = Flask(__name__)

@app.route('/sms', method=['POST'])
def handle_sms():
	user = request.form['From']
	pet = request.form['Body'].strip().lower()

if __name__ == '__main__':
	app.run(debug=True)
