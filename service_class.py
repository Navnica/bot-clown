import models
import tabulate
import jokemanager


class CategoryManager:
    def __init__(self, category_id) -> None:
        self.category: models.JokeCategory = models.JokeCategory.get_or_none(models.JokeCategory.id == category_id)

    def add(self, name: str, url: str) -> None:
        models.JokeCategory.create(name=name, url=url).save()

    def remove(self) -> None:
        self.category.delete_instance()

    def show_all(self) -> None:
        print(tabulate.tabulate(models.JokeCategory.select().dicts()))

    def dump(self) -> None:
        jokes = jokemanager.parse_all_jokes(self.category.url)

        for joke in jokes:
            JokeManager(joke['data_id']).remove()
            JokeManager().add(
                category=self.category,
                text=joke['text'],
                rating=joke['rating'],
                data_id=joke['data_id']
            )


class JokeManager:
    def __init__(self, joke_id=None) -> None:
        self.joke: models.Joke = models.Joke.get_or_none(models.Joke.data_id == joke_id)

    def add(self, category: models.JokeCategory, text: str, rating: int, data_id: int) -> None:
        models.Joke.create(
            category_id=category.id,
            text=text,
            rating=rating,
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

    def change_rating(self, new_rating: int) -> None:
        self.joke.rating += new_rating
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


class Service:
    def __init__(self, category_id=None, joke_id=None, user_id=None) -> None:
        self.category = CategoryManager(category_id)
        self.joke = JokeManager(joke_id)
        self.user = UserManager(user_id)
