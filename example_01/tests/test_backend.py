import pytest
from example_01.backend import statement


@pytest.fixture
def plays():
    return {
        "hairspray": {
            "name": "Hairspray",
            "type": "comedy"
        },
        "o-lago-dos-cisnes": {
            "name": "O Lago dos Cisnes",
            "type": "tragedy"
        }
    }


@pytest.fixture
def invoice():
    return {
        "customer": "LittleCo",
        "performances": [
            {
                "playID": "hairspray",
                "audience": "45"
            },
            {
                "playID": "o-lago-dos-cisnes",
                "audience": "30"
            }
        ]
    }


def test_statement(invoice, plays):
    result = statement(invoice, plays)

    assert result == (
        'Statement for LittleCo\n'
        'Hairspray: 570.0 (45 seats)\n'
        'O Lago dos Cisnes: 400.0 (30 seats)\n'
        'Amount owed is 970.0\n'
        'You earned 24 credits\n'
    )
