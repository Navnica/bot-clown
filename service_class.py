import models
import tabulate
import parser
import random


class CategoryManager:
    def __init__(self, category_id=None) -> None:
        self.category: models.JokeCategory = models.JokeCategory.get_or_none(models.JokeCategory.id == category_id)

    def add(self, name: str, url: str, autodump=False) -> None:
        self.category = models.JokeCategory.create(name=name, url=url)
        self.category.save()
        if autodump:
            self.dump()

    def get(self) -> models.JokeCategory:
        return self.category

    def remove(self) -> None:
        self.category.delete_instance()

    def show_all(self) -> None:
        print(tabulate.tabulate(models.JokeCategory.select().dicts()))

    def random_joke(self) -> models.Joke:
        return random.choice(models.Joke.select().where(models.Joke.category_id == self.category))

    def list(self):
        return models.JokeCategory.select()

    def dump(self) -> None:
        jokes = parser.parse_all_jokes(self.category.url)

        for joke in jokes:
            JokeManager(joke['data_id']).remove()
            JokeManager().add(
                category=self.category,
                text=joke['text'],
                data_id=joke['data_id']
            )


class JokeManager:
    def __init__(self, joke_id=None) -> None:
        self.joke: models.Joke = models.Joke.get_or_none(models.Joke.id == joke_id)

    def add(self, category: models.JokeCategory, text: str, data_id: int) -> None:
        models.Joke.create(
            category_id=category.id,
            text=text,
            data_id=data_id
        )

    def remove(self) -> None:
        if self.joke is None:
            return None

        self.joke.delete_instance()

    def get(self) -> models.Joke:
        return self.joke

    def get_information(self) -> None:
        print(tabulate.tabulate([self.joke.id, self.joke.text, self.joke.rating], headers=['id', 'text', 'rating']))

    def rate_plus(self) -> None:
        self.joke.rate_plus += 1
        self.joke.save()

    def rate_minus(self) -> None:
        self.joke.rate_minus += 1
        self.joke.save()


class UserManager:
    def __init__(self, user_id=None) -> None:
        self.user = models.User.get_or_none(models.User.telegram_id == user_id)
        self.user_id = user_id

    def add(self) -> None:
        models.User.create(telegram_id=self.user_id)

    def set_category(self, category: models.JokeCategory):
        self.user.category = category
        self.user.save()

    def set_message(self, message_id: int) -> None:
        self.user.message_id = message_id
        self.user.save()

    def get(self) -> models.User:
        return self.user

    def show_all(self):
        print(tabulate.tabulate(models.User.select().dicts()))


class RateManager:
    def __init__(self, rate_id=None) -> None:
        self.rate = models.JokeRating.get_or_none(models.JokeRating.id == rate_id)

    def add(self, user_id, joke, rate_plus) -> None:
        models.JokeRating.create(
            joke_id=models.Joke.get(models.Joke.id == joke),
            user_id=models.User.get(models.User.telegram_id == user_id),
            rate_plus=rate_plus
        )

        manager = JokeManager(joke.id)
        manager.rate_plus() if rate_plus else manager.rate_minus()

    def get(self) -> models.JokeRating:
        return self.rate


class Service:
    def __init__(self, category_id=None, joke_id=None, user_id=None, rate_id=None) -> None:
        self.category = CategoryManager(category_id)
        self.joke = JokeManager(joke_id)
        self.user = UserManager(user_id)
        self.rate = RateManager(rate_id)
