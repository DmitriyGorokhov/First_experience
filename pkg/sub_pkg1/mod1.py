import csv
from pprint import pprint

def API_to_CSV(API_info):
    try:
        with open('API_to_CSV_file.csv', 'w', encoding='UTF-8') as API_to_CSV_file:
            csv_writer = csv.DictWriter(API_to_CSV_file, fieldnames=list(API_info.keys()))
            csv_writer.writeheader()
            csv_writer.writerow(API_info)
    except Exception as e:
        pprint(f"Information is not write in file 'API_to_CSV_file.csv'! Error -{e}")

