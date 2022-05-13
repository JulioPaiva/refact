from math import floor
import json

with open("plays.json", encoding='utf-8') as _json:
    plays = json.load(_json)

with open("invoices.json", encoding='utf-8') as _json:
    invoice = json.load(_json)


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    for p in invoice['performances']:
        play = plays[p['playID']]
        this_amount = 0
        audience = int(p['audience'])

        if play['type'] == 'tragedy':
            this_amount = 40000
            if audience > 30:
                this_amount += 1000 * (audience - 30)

        elif play['type'] == 'comedy':
            this_amount = 30000
            if audience > 20:
                this_amount += 1000 + 500 * (audience - 20)
            this_amount += 300 * audience
        else:
            raise

        volume_credits += max(audience - 30, 0)

        if play['type'] == 'comedy':
            volume_credits += floor(audience/5)

        result += f'{play["name"]}: {this_amount/100} ({p["audience"]} seats)\n'  # noqa
        total_amount += this_amount

    result += f'Amount owed is {total_amount/100}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


print(statement(invoice[0], plays))
