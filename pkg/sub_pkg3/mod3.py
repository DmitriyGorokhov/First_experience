import json
from pprint import pprint

def API_to_TXT(API_info):
    try:
        with open('API_to_TXT_file.txt', 'w') as API_to_TXT_file:
            json.dump(API_info, API_to_TXT_file)
    except Exception as e:
        pprint(f"Information is not write in file 'API_to_TXT_file.txt'! Error -{e}")