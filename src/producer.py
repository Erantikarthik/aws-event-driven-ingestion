
import json
from pathlib import Path


def load_event():
    file_path = Path(__file__).parent.parent / "events" / "sample_order.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_event(event):
    required_fields = [
        "event_id",
        "event_type",
        "order_id",
        "customer_id",
        "amount",
        "quantity",
    ]

    for field in required_fields:
        if field not in event:
            raise ValueError(f"Missing required field: {field}")

    if event["amount"] < 0:
        raise ValueError("Amount cannot be negative")

    if event["event_type"] != "ORDER_CREATED":
        raise ValueError("Invalid event type")

    if event["quantity"] <= 0:
        raise ValueError("Quantity must be greater than zero")

    return True


if __name__ == "__main__":
    event = load_event()
    validate_event(event)
    print("Event loaded and validated successfully!")
    print(json.dumps(event, indent=2))
