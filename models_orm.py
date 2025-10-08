from peewee import *

db = SqliteDatabase('data.db')


def create_db():
    db.connect()
    db.create_tables([Group, Street, KindOfGarbage, Date])
    return db


class Group(Model):
    name = TextField()

    class Meta:
        database = db


class Street(Model):
    group = ForeignKeyField(Group, backref='streets')
    name = TextField()

    class Meta:
        database = db


class KindOfGarbage(Model):
    name = TextField()

    class Meta:
        database = db


class Date(Model):
    group = ForeignKeyField(Group, backref='dates')
    kind_of_garbage = ForeignKeyField(KindOfGarbage, backref='dates')
    january = TextField(null=True)
    february = TextField(null=True)
    march = TextField(null=True)
    april = TextField(null=True)
    may = TextField(null=True)
    june = TextField(null=True)
    july = TextField(null=True)
    august = TextField(null=True)
    september = TextField(null=True)
    october = TextField(null=True)
    november = TextField(null=True)
    december = TextField(null=True)

    class Meta:
        database = db
