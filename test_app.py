
import pytest
from app import BankAccount


def test_initial_balance():
    account = BankAccount(1000)
    assert account.check_balance() == 1000


def test_deposit():
    account = BankAccount(1000)
    assert account.deposit(500) == 1500


def test_withdraw():
    account = BankAccount(1000)
    assert account.withdraw(200) == 800


def test_insufficient_balance():
    account = BankAccount(1000)

    with pytest.raises(ValueError, match="Insufficient balance"):
        account.withdraw(2000)


def test_negative_deposit():
    account = BankAccount(1000)

    with pytest.raises(ValueError):
        account.deposit(-100)

