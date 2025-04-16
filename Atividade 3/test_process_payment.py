import pytest
import random
from process_payment import process_payment, InvalidPaymentDetails, PaymentGatewayError

def test_invalid_user_id():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("", 100)

def test_invalid_amount():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("Admin", -2)

def test_unsupported_currency():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("Admin", 100, currency="BRL")


def test_payment_gateway_error(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.1)  # Sempre falha

    with pytest.raises(PaymentGatewayError):
        process_payment("user123", 100, retries=2)


def test_successful_payment(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.5)
    monkeypatch.setattr(random, "randint", lambda a, b: 123456)
    
    result = process_payment("user123", 100, currency="USD")
    assert result["status"] == "success"
    assert result["transaction_id"] == "TXN-123456"
    assert result["amount_charged"] == 100.0
    assert result["currency"] == "USD"
