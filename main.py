#! venv/bin/python3
import sys
from load_json_file import load_data

data_file="./wykaz_2025.json"

def main():
    print(f'PYTHON: {sys.version}')

if __name__=='__main__':
    main()
    # -----------------------------------------------------------------
    user_street=[]
    user_area=''

    user_input_street=''
    # -----------------------------------------------------------------
    if len(sys.argv)>1:
        if "street" in sys.argv[1]:
            user_input_street=sys.argv[2].lower()
    # -----------------------------------------------------------------
    data=load_data(data_file)
    # print(data)
    if data and isinstance(data, dict):
        print(data.keys())
    # -----------------------------------------------------------------
    for e in data["Rejony_Ulice"]:
        temp_streets = e["Ulice"].split(', ')
        for street in temp_streets:
            if user_input_street in street.lower():
                user_street.append(street)
                user_area=e["Rejon"]

    if len(user_street) == 0:
        print('Nie znaleziono podanej ulicy.')
    elif len(user_street)==1:
        print(user_area)
        print(user_street)
    elif len(user_street) >1:
        print('Sprecyzuj nazwe ulicy.')
        print(user_street)
    # -----------------------------------------------------------------