# Corotos-Pet-Finder

With Corotos-Pet-Finder you can set up searches for specific pets on the corotos web site (a craigslist-like website in the Dominican Republic) via text message and get a text notification when someone posts a matching offer.
This service saves you multiple visits to the site in order to find the pet of your dreams.


Check out my [LinkedIn](https://www.linkedin.com/in/vanesaortiz) profile for more information on my experience, education, and projects.

### Contents

- [Overview](#overview)
- [Technologies & Stack](#technologies-and-stack)
- [Features](#features)
- [Screenshots](#screenshots)


Overview
----------------

Corotos-Pet-Finder helps you find a pet on the Corotos Web Site:
* by creating a subscription via text message
* scraping the Corotos Website and notifying the subscribers via text message if there is a match
* storing multiple subscriptions on Redis
* summing up multiple matches per scrape into one text message


Technologies and stack
------------------------

#### Backend
Python, Beautiful Soup, Redis

#### APIs:
Twilio.


Features
-------------------

- [x] Set up pet search through text message

- [x] Scrape Corotos Website with Beautiful Soup for matches.

- [x] Store subscriptions via Redis.

- [x] Receive matches summed up in a single text message


##### APIs
- [x] Twilio API integration allows users to set up their search via text message and also receive the notification for matches.


Screenshots
-----------------------

###### Coming Soon!


Forking?
-----------------------
You'll need your own API keys for Twilio!

	pip install -r requirements.txt

	create a secrets.py which contains the following variables:
		twilio_account_sid = "[YOUR TWILIO ACCOUND SID]"
		token = "[YOUR TWILIO TOKEN]"
		my_number = "[YOUR TWILIO NUMBER]"
	
	redis-server

	(If you want to monitor the calls) redis-cli >> monitor

	You can use ngrok (https://ngrok.com/) to create a public URL to a local webserver on your machine

	Set up the messaging web hook for your twilio number to your ngrok url + "/sms"

	python sms_handler.py

	Send a text message to your Twilio number with the type of pet you're searching for e.g. "Shihtzu"

	python scraper.py

