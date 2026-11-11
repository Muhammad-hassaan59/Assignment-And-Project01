import pytest

from bank_account import BankAccount


@pytest.fixture
def account():
    """Provide a fresh account with Rs 1000 for each test."""
    return BankAccount(1000)


def test_deposit(account):
    assert account.deposit(500) == 1500
    assert account.balance == 1500


def test_withdraw(account):
    assert account.withdraw(300) == 700
    assert account.balance == 700


def test_history_list(account):
    account.deposit(200)
    account.withdraw(100)
    assert account.history == [
        "Deposited Rs 200",
        "Withdrew Rs 100",
    ]


def test_withdraw_more_than_balance_raises_error(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(1500)


def test_non_positive_deposit_raises_error(account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(0)
