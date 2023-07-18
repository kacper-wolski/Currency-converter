import requests
import json
from time import time


def data_request():

    file_path = "Files/currency_data.json"
    current_time = int(time())

    with open(file_path, "r") as file:
        currency_data = json.load(file)

    timestamp = currency_data.get('timestamp', None)
    time_diff = current_time - timestamp


    if time_diff == 3600 or time_diff > 3600:
        json_file = requests.get('https://openexchangerates.org/api/latest.json?app_id=50414afc19ae4c14a63fda13f1d1500e')

        if json_file.status_code == 200:
            currency_data = json_file.json()

            with open(file_path, "w") as file:
                json.dump(currency_data, file)

    return currency_data