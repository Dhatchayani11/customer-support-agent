
from mcp.server.fastmcp import FastMCP

from .order_tools import (
    get_order,
    get_customer,
    get_delivery_status,
    get_customer_orders,
)

# Initialize the MCP server
mcp = FastMCP("customer-support-mcp-server")


@mcp.tool()
def lookup_order(order_id: str) -> dict:
    """Retrieve order details using an order ID."""
    return get_order(order_id)


@mcp.tool()
def lookup_customer(customer_id: str) -> dict:
    """Retrieve customer information using a customer ID."""
    return get_customer(customer_id)


@mcp.tool()
def lookup_delivery(order_id: str) -> dict:
    """Retrieve delivery status and tracking information."""
    return get_delivery_status(order_id)


@mcp.tool()
def lookup_customer_orders(customer_id: str) -> dict:
    """Retrieve all orders associated with a customer."""
    return get_customer_orders(customer_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
