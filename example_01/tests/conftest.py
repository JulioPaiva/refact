import pytest


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
