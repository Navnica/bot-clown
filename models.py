import peewee

db = peewee.SqliteDatabase('database.db')


class JokeCategory(peewee.Model):
    category_id = peewee.IntegerField(null=False)
    category_name = peewee.CharField(null=False)
    url = peewee.Еуче

    class Meta:
        database = db


class User(peewee.Model):
    telegram_id = peewee.IntegerField(null=False)
    message_id = peewee.IntegerField(null=False)
    category = peewee.ForeignKeyField(JokeCategory, related_name='category_id')

    class Meta:
        database = db


