from math import floor
import json


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    for p in invoice['performances']:

        volume_credits += max(int(p['audience']) - 30, 0)

        if play_for(p)['type'] == 'comedy':
            volume_credits += floor(int(p['audience'])/5)

        result += '{name}: {amount} ({audience} seats)\n'.format(
            name=play_for(p)['name'],
            amount=amount_for(p)/100,
            audience=p["audience"]
        )

        total_amount += amount_for(p)

    result += f'Amount owed is {total_amount/100}\n'
    result += f'You earned {volume_credits} credits\n'

    return result


def amount_for(a_perf):
    result = 0

    if play_for(a_perf)['type'] == 'tragedy':
        result = 40000
        if int(a_perf['audience']) > 30:
            result += 1000 * (int(a_perf['audience']) - 30)

    elif play_for(a_perf)['type'] == 'comedy':
        result = 30000
        if int(a_perf['audience']) > 20:
            result += 1000 + 500 * (int(a_perf['audience']) - 20)
        result += 300 * int(a_perf['audience'])
    else:
        raise

    return result


def play_for(a_perf):
    return plays[a_perf['playID']]


with open("example_01/plays.json", encoding='utf-8') as _json:
    plays = json.load(_json)

with open("example_01/invoices.json", encoding='utf-8') as _json:
    invoice = json.load(_json)

print(statement(invoice[0], plays))
