import peewee

db = peewee.SqliteDatabase('database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class JokeCategory(BaseModel):
    name = peewee.CharField(null=False)
    url = peewee.CharField()

    def __str__(self):
        return self.name


class User(BaseModel):
    telegram_id = peewee.IntegerField(null=False)
    message_id = peewee.IntegerField(null=True, default=None)
    category = peewee.ForeignKeyField(JokeCategory, related_name='category_id', null=True, default=None)


class Joke(BaseModel):
    category_id = peewee.ForeignKeyField(JokeCategory, related_name='category_id')
    text = peewee.TextField()
    rating = peewee.IntegerField(default=0)


JokeCategory.create_table()
User.create_table()
Joke.create_table()