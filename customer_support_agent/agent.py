
from google.adk.agents import Agent
from .order_tools import get_order

root_agent = Agent(
    name="customer_support_agent",
    model="gemini-3.8-flash",
    description="An AI agent that investigates e-commerce customer complaints.",
    instruction="""
    You are a customer support investigation assistant.

    When a customer provides an order ID and asks about their order,
    use the get_order tool to retrieve the order details.

    Explain the retrieved information accurately.
    If an order is not found, tell the customer that the order
    could not be found.

    Never invent order details.
    Never promise a refund, replacement, or escalation without
    verified information and authorization.
    """,
    tools=[get_order],
)
