import json
from pprint import pprint

def API_to_JSON(API_info):
    try:
        with open('API_to_JSON_file.json', 'w') as API_to_JSON_file:
            json.dump(json.dumps(API_info), API_to_JSON_file)
    except Exception as e:
        pprint(f"Information is not write in file 'API_to_JSON_file.json'! Error -{e}")