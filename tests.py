import pytest
from unittest.mock import patch
from functions import randomnumbers, randomgame, verify

def test_randomnumbers():
    number = randomnumbers()
    assert 1 <= number <= 100, "O número deve ser entre 1 a 100"

def test_randomgame_correct_guess():
    number = 50
    with patch('builtins.input', return_value='50'):
        result = randomgame(number)
        assert result == True, "o jogo precisará retornar True"

def test_randomgame_incorrect_guess():
    number = 50
    with patch('builtins.input', return_value='30'):
        result = randomgame(number)
        assert result == 30, "o jogo deve retornar o número de usuário se estiver"

def test_verify_greater():
    result = verify(50, 30)
    assert result == 'O número sorteado é maior', "precisa indicar que o número é maior"

def test_verify_smaller():
    result = verify(50, 70)
    assert result == 'O número sorteado é menor', "precisa indicar que o número é maior"

def test_verify_equal():
    result = verify(50, 50)
    assert result == None, "deve retornar None quando os números são iguais"
