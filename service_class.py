import models
import tabulate


class CategoryManager:
    def __init__(self, category_id) -> None:
        self.category_id: models.JokeCategory = category_id

    def add_category(self, name: str, url: str) -> None:
        models.JokeCategory.create(name=name, url=url).save()

    def del_category(self) -> None:
        models.JokeCategory.get(models.JokeCategory.id == self.category_id).delete_instance()

    def show_all_category(self) -> None:
        print(tabulate.tabulate(models.JokeCategory.select().dicts()))


class JokeManager:
    def __init__(self, joke_id) -> None:
        self.joke_id: models.Joke = joke_id

    def add_joke(self, category_id: models.JokeCategory, text: str) -> None:
        models.Joke.create(category_id=category_id, text=text)

    def del_joke(self) -> None:
        models.Joke.get(models.Joke.id == self.joke_id)

    def get_joke(self) -> models.Joke:
        return models.Joke.get(models.Joke.id == self.joke_id)

    def get_joke_information(self) -> None:
        joke = models.Joke.get(models.Joke.id == self.joke_id)
        print(tabulate.tabulate([joke.id, joke.text, joke.rating], headers=['id', 'text', 'rating']))

    def change_joke_rating(self, update: int) -> None:
        joke = models.Joke.get(models.Joke.id == self.joke_id)
        joke.rating += update
        joke.save()


class UserManager:
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def add_user(self) -> None:
        models.User.create(telegram_id=self.user_id)

    def set_category(self, category: models.JokeCategory):
        user = models.User.get(models.User.telegram_id == self.user_id)
        user.category = category
        user.save()

    def set_message(self, message_id: int) -> None:
        user = models.User.get(models.User.telegram_id == self.user_id)
        user.message_id = message_id
        user.save()

    def get_user(self) -> models.User:
        return models.User.get(models.User.telegram_id == self.user_id)

    def show_all_users(self):
        print(tabulate.tabulate(models.User.select().dicts()))


class Service:
    def __init__(self, category_id=None, joke_id=None, user_id=None) -> None:
        self.category = CategoryManager(category_id)
        self.joke = JokeManager(joke_id)
        self.user = UserManager(user_id)
