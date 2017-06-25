import requests
from bs4 import BeautifulSoup

URL = 'https://www.corotos.com.do/republica_dominicana/animales_y_mascotas-en_venta'
PET_NUM_NDX = 0
 
def get_puppies():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    pets = []
    found_pet = False
 
    for titles in soup.find_all('h2'):
        links = [e.text for e in titles.find_all('a')]
        if links:
            pets.append(links[PET_NUM_NDX])

    for pet in pets:
    	if 'pitbull' in pet.lower():
    		found_pet = True 
    
    return 'Found Pet: ', found_pet