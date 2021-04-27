# To be removed ----

import requests
import json

url = requests.get('https://www.sreality.cz/api/cs/v2/estates/1961732700')

url_json = (json.loads(url.text))

# To be removed ----



def extract_area(json):
    for value in range(len(json['items'])):
        if json['items'][value]['name'] == 'Užitná plocha':
             area =  int(json['items'][value]['value'])
    return (area)
