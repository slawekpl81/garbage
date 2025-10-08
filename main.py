#! venv/bin/python3
import sys
from pathlib import Path
from bottle import route, run, template

from load_json_file import load_data

data_file = "./wykaz_2025.json"

from models_orm import *
from routes import *


def main():
    print(f'PYTHON: {sys.version}')


if __name__ == '__main__':
    main()

    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
    if not Path('data.db').is_file():
        # -----------------------------------------------------------------
        # load data from json
        data = load_data(data_file)
        # -----------------------------------------------------------------
        # create database
        db = create_db()
        # -----------------------------------------------------------------
        # insert data to db
        for element in data["harmonogram_odbioru_odpadow"]["rejony"]:
            group = Group.create(name=element["nazwa_rejonu"])
            for street_name in element["ulice"]:
                street = Street.create(group=group, name=street_name)

            for kind, values in element['harmonogramy'].items():
                # print(kind)
                temp_kind, created = KindOfGarbage.get_or_create(name=kind)
                # print(f'{temp_kind}--{created}')

                temp_date = Date.create(group=group, kind_of_garbage=temp_kind)
                temp_date.january = ", ".join(map(str, values.get('STYCZEN', [])))
                temp_date.february = ", ".join(map(str, values.get('LUTY', [])))
                temp_date.march = ", ".join(map(str, values.get('MARZEC', [])))
                temp_date.april = ", ".join(map(str, values.get('KWIECIEN', [])))
                temp_date.may = ", ".join(map(str, values.get('MAJ', [])))
                temp_date.june = ", ".join(map(str, values.get('CZERWIEC', [])))
                temp_date.july = ", ".join(map(str, values.get('LIPIEC', [])))
                temp_date.august = ", ".join(map(str, values.get('SIERPIEN', [])))
                temp_date.september = ", ".join(map(str, values.get('WRZESIEN', [])))
                temp_date.october = ", ".join(map(str, values.get('PAŹDZIERNIK', [])))
                temp_date.november = ", ".join(map(str, values.get('LISTOPAD', [])))
                temp_date.december = ", ".join(map(str, values.get('GRUDZIEŃ', [])))
                temp_date.save()
        print('data loaded')
    # -----------------------------------------------------------------
    # BOTTLE
    run(host='localhost', port=8080, debug=True, reloader=True)
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    # -----------------------------------------------------------------

    # -----------------------------------------------------------------
