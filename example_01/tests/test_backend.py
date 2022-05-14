import pytest
from example_01.backend import statement


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
