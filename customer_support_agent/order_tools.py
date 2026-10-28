
import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "orders.json"


def get_order(order_id: str) -> dict:
    """Retrieve an order using its order ID."""

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    for order in data["orders"]:
        if order["order_id"] == order_id:
            return order

    return {"error": f"Order {order_id} was not found."}


if __name__ == "__main__":
    print(get_order("ORD9999"))
