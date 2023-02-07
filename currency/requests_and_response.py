import json
import iso4217parse as iso42
import requests


def get_requests():
    API_KEY = 'gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR'
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
    resp = requests.get(url)

    data = json.loads(resp.text)

    with open('currency.json', 'w') as f:
        json.dump(data, f)

    res = {}
    with open('currency.json') as f:
        data_load = json.load(f)
        data = data_load.get('data')
        for k, v in data.items():
            name = iso42.by_symbol_match(k)
            res[name[0][2]] = k

    with open('currency_short_and_long_name.json', 'w') as f:
        json.dump(res, f)
