from bottle import route, template
from models_orm import *


@route('/hello')
def hello():
    return template('hello')


@route('/groups')
def groups():
    query = Group.select()
    return template('groups', groups=query)


@route('/group/<name>')
def group(name):
    query = Group.get_or_none(name=name)
    if query:
        streets = query.streets.select()
    else:
        streets = {name: 'dupa'}

    return f' {[street.name for street in streets]}'
