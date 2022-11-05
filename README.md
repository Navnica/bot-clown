# Bot Clown

As the great Chinese philosopher San Hui Sun said in 739 BC
>As my good friend San Hui Win said, literally EVERY person's dream on earth is to go to Telegram at any moment to get a random joke from a 2002-year Russian web-site.

This bot solves this problem.
With the help of the latest gen technologies

## Features.
- No clogging of the chat with a large number of messages. With using InlineKeyboard.
- The ability to download any category of jokes from the site [anekdot.ru](https://anekdot.ru/tags)
- Partial database management via the command-line interface
- Emoji.

## Tech

| Lib                    | PyPi                                            |
|------------------------|-------------------------------------------------|
| PyTelegramBotApi 4.7.1 | https://pypi.org/project/pyTelegramBotAPI/4.7.1 |
| BeautifulSoup4 4.11.1  | https://pypi.org/project/beautifulsoup4/4.11.1  |
| cowsay 5.0             | https://pypi.org/project/cowsay/5.0             |
| requests 2.28.1        | https://pypi.org/project/requests/2.28.1        |
| peewee 3.15.3          | https://pypi.org/project/peewee/3.15.3          |
| fire 0.4.0             | https://pypi.org/project/fire/0.4.0/            |
| tabulate 0.9.0         | https://pypi.org/project/tabulate/0.9.0/        |

## Running

The bot comes without a filled database, so before launching it, you MUST look through the Service section, add and dump at least one category
How to make it read in [Service](#service)

Add your token in config.json

```commandline
git clone https://github.com/TruEn0t/bot-clown.git
cd bot-clown
pip3 install -r requirements.txt
python3 main.py
```

If at Windows you get `python3.exe command not found` try to use `python` instead `python3`

## Service
Using service.py you can partially manage the database for the bot.
Add, delete, view categories, users and jokes

For example
```commandline
python service.py category add --name=Водка --url=https://www.anekdot.ru/tags/водка
python service.py category dump --category_id=1
```
With the first command, we add the category of jokes to the database, 
after which we give the command to parse jokes from the site

The request can be reduced to a single command by passing `autodump=True`

```commandline
python service.py category add --name=Путин --url=https://www.anekdot.ru/tags/Путин --autodump=True
```

If we execute 
```commandline
python service.py category show_all
```
we will see something like the following
```
-  -----  ---------------------------------
1  Водка  https://www.anekdot.ru/tags/водка
2  Путин  https://www.anekdot.ru/tags/Путин
-  -----  ---------------------------------
```

Use `python service.py wtf` to get more commands