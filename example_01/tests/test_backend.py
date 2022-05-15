import pytest
from unittest import mock
from example_01.backend import statement, amount_for, play_for


@mock.patch('example_01.backend.play_for')
def test_statement_should_return_success(mock, invoice, plays):

    mock.return_value = {"name": "Hairspray", "type": "comedy"}
    del invoice['performances'][-1]
    result = statement(invoice, plays)

    assert result == (
        'Statement for LittleCo\n'
        'Hairspray: 570.0 (45 seats)\n'
        'Amount owed is 570.0\n'
        'You earned 24 credits\n'
    )


def test_statement_should_return_error_with_type_invalid(invoice):
    plays = {
        "hairspray": {
            "name": "Wheee",
            "type": "blablabla"
        }
    }

    with pytest.raises(Exception):
        statement(invoice, plays)


def test_amount_for_should_return_error():
    play = {
        "hairspray": {
            "name": "Wheee",
            "type": "blablabla"
        }
    }

    with pytest.raises(Exception):
        amount_for(50, play)


def test_play_for_should_return_success():
    result = play_for({'playID': 'hamlet'})

    assert result['name']
    assert result['type']
