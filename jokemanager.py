from bs4 import BeautifulSoup
import requests
import json
import random


def parse_all_jokes(url) -> None:
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
