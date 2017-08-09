from bs4 import BeautifulSoup
import requests
import redis
import time
from twilio.rest import Client
from secrets import twilio_account_sid, token, my_number


URL = 'https://www.corotos.com.do/republica_dominicana/animales_y_mascotas-en_venta'
PET_NUM_NDX = 0

def get_pets():

    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    pets = []
 
    for titles in soup.find_all('h2'):
        links = [e.text for e in titles.find_all('a')]
        if links:
            pets.append(links[PET_NUM_NDX].strip())

    return pets

client = Client(twilio_account_sid, token)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
 
def message(recipient, body):
    message = client.messages.create(to=recipient, from_=my_number, body=body)
 
 
if __name__ == '__main__':
    pets = get_pets()
    for pet in pets:
        if 'johnson' or 'king charles' not in pet.lower():
            continue
 
        to_notify = redis_client.smembers(pet)
        for user in to_notify:
            message(user.decode('utf-8'), body="Good news! We found a {pet}.")
            redis_client.srem(pet, user)
