## Testes para um validador de E-mails
## Maria Clara Almeida Galvao - 156.592

""" Lógica do Teste: Verifica-se um padrão Regex, que valida se um email é válido ou não
## JSON é responsável por conter as entradas que serão validas dentro do validador e consequentemente, se 
são entradas válidas ou não. """

import re
import json
import pytest

def padraoEmail(email):
    regex = r'[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
    return re.match(regex, email) is not None

## Entradas do Teste feitos a partir de um JSON
## Para rodar os testes: pytest validadorEmailsTest.py

def importTests():
    with open('inputs.json', 'r') as file:
        inputs = json.load(file)
        for input in inputs:
            yield input['email'], input['valid']

@pytest.mark.parametrize("email, valid", importTests())
def testEmail(email, valid):
    assert padraoEmail(email) == valid

