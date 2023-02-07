import json


def convert(from_currency, to_currency, amount):
    with open('currency.json') as f:
        data = json.load(f).get('data')
    initial_amount = amount

    if from_currency != 'USD':
        amount = amount / data.get(from_currency)

    amount = round(amount * data[to_currency], 2)
    res = ('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
    return res

