import pytest
from unittest import mock
from example_01.backend import statement, amount_for, play_for, format_real


@mock.patch('example_01.backend.play_for')
def test_statement_should_return_success(mock, invoice, plays):

    mock.return_value = {"name": "Hairspray", "type": "comedy"}
    del invoice['performances'][-1]
    result = statement(invoice, plays)

    assert result == (
        'Statement for LittleCo\n'
        'Hairspray: R$ 570.00 (45 seats)\n'
        'Amount owed is R$ 570.00\n'
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


@pytest.mark.parametrize('number, expected', [
    (-100, 'R$ -1.00'), (0, 'R$ 0.00'), (200, 'R$ 2.00'), (200.500, 'R$ 2.00'),
    (1000, 'R$ 10.00'), (1000.1, 'R$ 10.00'), (1010.123456789, 'R$ 10.10')]
)
def test_format_real_should_return_success(number, expected):
    result = format_real(number)

    assert result == expected
