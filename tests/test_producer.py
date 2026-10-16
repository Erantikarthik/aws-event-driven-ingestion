
import pytest
from src.producer import load_event, validate_event


def test_load_event():
    event = load_event()

    assert event["event_id"] == "evt-1001"
    assert event["event_type"] == "ORDER_CREATED"
    assert event["order_id"] == "ORD-1001"
    assert event["amount"] == 1499.00


def test_valid_event():
    event = load_event()
    assert validate_event(event) is True


def test_negative_amount():
    event = load_event()
    event["amount"] = -100

    with pytest.raises(ValueError, match="Amount cannot be negative"):
        validate_event(event)


def test_missing_required_field():
    event = load_event()
    del event["order_id"]

    with pytest.raises(ValueError, match="Missing required field: order_id"):
        validate_event(event)


def test_invalid_event_type():
    event = load_event()
    event["event_type"] = "INVALID_EVENT"

    with pytest.raises(ValueError, match="Invalid event type"):
        validate_event(event)


def test_missing_event_id():
    event = load_event()
    del event["event_id"]

    with pytest.raises(ValueError, match="Missing required field: event_id"):
        validate_event(event)


def test_invalid_quantity():
    event = load_event()
    event["quantity"] = 0

    with pytest.raises(
        ValueError, match="Quantity must be greater than zero"
    ):
        validate_event(event)


def test_missing_quantity():
    event = load_event()
    del event["quantity"]

    with pytest.raises(ValueError, match="Missing required field: quantity"):
        validate_event(event)
