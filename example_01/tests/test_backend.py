import pytest
from example_01.backend import statement, amount_for


def test_statement_should_return_success(invoice, plays):
    result = statement(invoice, plays)

    assert result == (
        'Statement for LittleCo\n'
        'Hairspray: 570.0 (45 seats)\n'
        'O Lago dos Cisnes: 400.0 (30 seats)\n'
        'Amount owed is 970.0\n'
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


@pytest.mark.parametrize('a_perm, play, expected', [
    (-5, 'tragedy', 40000),
    (-5, 'comedy', 28500),
    (0, 'tragedy', 40000),
    (0, 'comedy', 30000),
    (10, 'tragedy', 40000),
    (10, 'comedy', 33000),
    (50, 'tragedy', 60000),
    (50, 'comedy', 61000),
])
def test_amount_for_should_return_success(a_perm, play, expected):
    _play = {'type': play}
    result = amount_for(a_perm, _play)

    assert result == expected


def test_amount_for_should_return_error():
    play = {
        "hairspray": {
            "name": "Wheee",
            "type": "blablabla"
        }
    }

    with pytest.raises(Exception):
        amount_for(50, play)
