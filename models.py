import peewee

db = peewee.SqliteDatabase('database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class JokeCategory(BaseModel):
    name = peewee.CharField(null=False, unique=True)
    url = peewee.CharField(null=False, unique=True)

    def __str__(self):
        return self.name


class User(BaseModel):
    telegram_id = peewee.IntegerField(null=False)
    message_id = peewee.IntegerField(null=True, default=None)
    category = peewee.ForeignKeyField(JokeCategory, related_name='category_id', null=True, default=None)


class Joke(BaseModel):
    category_id = peewee.ForeignKeyField(JokeCategory, related_name='category_id')
    text = peewee.TextField(null=False, unique=True)
    rate_plus = peewee.IntegerField(default=0)
    rate_minus = peewee.IntegerField(default=0)
    data_id = peewee.IntegerField(null=False)


class JokeRating(BaseModel):
    joke_id = peewee.ForeignKeyField(Joke, null=False, related_name='joke_id')
    user_id = peewee.ForeignKeyField(User, null=False, related_name='user_id')
    rate_plus = peewee.BooleanField(null=False)


JokeCategory.create_table()
User.create_table()
Joke.create_table()
JokeRating.create_table()
