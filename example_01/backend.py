from math import floor
import json


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    for p in invoice['performances']:
        play = plays[p['playID']]
        audience = int(p['audience'])

        this_amount = amount_for(audience, play)

        volume_credits += max(audience - 30, 0)

        if play['type'] == 'comedy':
            volume_credits += floor(audience/5)

        result += f'{play["name"]}: {this_amount/100} ({p["audience"]} seats)\n'  # noqa
        total_amount += this_amount

    result += f'Amount owed is {total_amount/100}\n'
    result += f'You earned {volume_credits} credits\n'

    return result


def amount_for(a_perm, play):
    result = 0

    if play['type'] == 'tragedy':
        result = 40000
        if a_perm > 30:
            result += 1000 * (a_perm - 30)

    elif play['type'] == 'comedy':
        result = 30000
        if a_perm > 20:
            result += 1000 + 500 * (a_perm - 20)
        result += 300 * a_perm
    else:
        raise

    return result


with open("example_01/plays.json", encoding='utf-8') as _json:
    plays = json.load(_json)

with open("example_01/invoices.json", encoding='utf-8') as _json:
    invoice = json.load(_json)

print(statement(invoice[0], plays))
