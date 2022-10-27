from bs4 import BeautifulSoup
import requests
import json
import random

category = json.load(open('config.json', encoding='utf-8'))['category']


def get_anek_with_category(category_name) -> str:
    soup = BeautifulSoup(requests.get(category[category_name]).text, "html.parser")
    list_anek = soup.findAll('div', class_='text')
    random_anek = random.choice(list_anek)
    return random_anek.text

