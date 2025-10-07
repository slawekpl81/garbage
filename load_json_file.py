import json

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as data_file:
            data_app=json.load(data_file)
    except FileNotFoundError:
        print(f"Error: Dont find '{filename}'.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Bad json format.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

    return data_app