
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent


def load_data(filename: str) -> dict:
    """Load JSON data from the customer support data directory."""
    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_order(order_id: str) -> dict:
    """Retrieve order details using an order ID."""
    data = load_data("orders.json")

    for order in data["orders"]:
        if order["order_id"] == order_id:
            return order

    return {"error": f"Order {order_id} was not found."}


def get_customer(customer_id: str) -> dict:
    """Retrieve customer information using a customer ID."""
    data = load_data("customers.json")

    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
            return customer

    return {"error": f"Customer {customer_id} was not found."}


def get_delivery_status(order_id: str) -> dict:
    """Retrieve delivery and tracking information using an order ID."""
    data = load_data("deliveries.json")

    for delivery in data["deliveries"]:
        if delivery["order_id"] == order_id:
            return delivery

    return {"error": f"Delivery information for {order_id} was not found."}


def get_customer_orders(customer_id: str) -> dict:
    """Retrieve all orders belonging to a customer."""
    data = load_data("orders.json")

    customer_orders = [
        order for order in data["orders"]
        if order["customer_id"] == customer_id
    ]

    if not customer_orders:
        return {
            "customer_id": customer_id,
            "orders": [],
            "message": "No orders found for this customer."
        }

    return {
        "customer_id": customer_id,
        "orders": customer_orders
    }


if __name__ == "__main__":
    print("\n--- ORDER ---")
    print(get_order("ORD1001"))

    print("\n--- CUSTOMER ---")
    print(get_customer("CUST101"))

    print("\n--- DELIVERY ---")
    print(get_delivery_status("ORD1001"))

    print("\n--- CUSTOMER ORDERS ---")
    print(get_customer_orders("CUST101"))
