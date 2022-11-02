from bs4 import BeautifulSoup
import requests


def parse_all_jokes(category: str) -> list:
    soup = BeautifulSoup(requests.get(category).text, "html.parser")
    count_of_pages: int = int(
        max([x.text for x in soup.find('div', class_='pageslist').findAll('a') if x.text.isdigit()]))
    joke_list = []

    for x in range(1, count_of_pages + 1):
        correct_url = f'{category}/{x}'
        jokes = BeautifulSoup(requests.get(correct_url).text, "html.parser").findAll('div', class_='topicbox')

        for joke in jokes:
            text = joke.find('div', class_='text')

            if text is None:
                continue

            joke_list.append({
                'text': BeautifulSoup(str(text).replace('<br/>', '\n'), 'html.parser').text,
                'data_id': int(joke['data-id'])
            })

    return joke_list
