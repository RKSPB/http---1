
import requests
import json

from pprint import pprint



def test_request():
    heroes_dict = {}
    sorted_dict = {}
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    for name in heroes_list:
        for q in response.json():
            if name == q.get('name'):
                intelligence = q.get('powerstats').get('intelligence')
                heroes_dict[name] = intelligence            
    sorted_keys = sorted(heroes_dict, key=heroes_dict.get)    
    for h in sorted_keys:
        sorted_dict[h] = heroes_dict[h]
    sorted_list = list(sorted_dict.items())
    print(f'Самый умный супергерой: {sorted_list[-1][0]}.  Статус ума: {sorted_list[-1][1]}')

test_request()



