from math import floor
import json


def statement(invoice, plays):
    total_amount = 0
    result = f'Statement for {invoice["customer"]}\n'

    for p in invoice['performances']:
        result += '{name}: {amount} ({audience} seats)\n'.format(
            name=play_for(p)['name'],
            amount=format_real(amount_for(p)),
            audience=p["audience"]
        )

        total_amount += amount_for(p)

    result += f'Amount owed is {format_real(total_amount)}\n'
    result += f'You earned {total_volume_credits()} credits\n'

    return result


def total_volume_credits():
    volume_credits = 0
    for p in invoice[0]['performances']:
        volume_credits += volume_credits_for(p)

    return volume_credits


def volume_credits_for(perf):
    volume_credits = max(int(perf['audience']) - 30, 0)
    if play_for(perf)['type'] == 'comedy':
        volume_credits += floor(int(perf['audience'])/5)

    return volume_credits


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


def format_real(a_number):
    return "R$ {:.2f}".format(a_number/100)


with open("example_01/plays.json", encoding='utf-8') as _json:
    plays = json.load(_json)

with open("example_01/invoices.json", encoding='utf-8') as _json:
    invoice = json.load(_json)

print(statement(invoice[0], plays))
