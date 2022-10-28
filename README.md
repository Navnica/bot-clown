# Bot Clown

As the great Chinese philosopher San Hui Sun said in 739 BC
>As my good friend San hui Win said, literally EVERY person's dream on earth is to go to Telegram at any moment to get a random joke from a 2002-year Russian web-site.

This bot solves this problem.
With the help of latest gen technologies

## Features
- Dynamic parse joke from web-site with jokes. No more repeates jokes never.
- No clogging of the chat with a large number of messages. With using InlineKeyboard.
- Three category jokes(may be more in future(anyone sure want most three? it's so many!))

## Tech

| Lib | PyPi |
| ------ | ------ |
| PyTelegramBotApi 4.7.1 | https://pypi.org/project/pyTelegramBotAPI/4.7.1 |
| BeautifulSoup4 4.11.1 | https://pypi.org/project/beautifulsoup4/4.11.1 |
| cowsay 5.0 | https://pypi.org/project/cowsay/5.0 |
| requests 2.28.1 | https://pypi.org/project/requests/2.28.1 |

## Running

```
git clone https://github.com/TruEn0t/bot-clown.git
cd bot-clown
pip3 install -r requirements.txt
python3 main.py
```

If at Windows you get `python3.exe command not found` try to use `python` instead `python3`
