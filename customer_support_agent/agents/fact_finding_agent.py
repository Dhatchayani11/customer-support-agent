
from pathlib import Path

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp import StdioServerParameters

from ..model_config import AGENT_MODEL


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MCP_SERVER_PARAMS = StdioServerParameters(
    command=str(PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"),
    args=[
        "-m",
        "customer_support_agent.mcp_server",
    ],
)

fact_finding_agent = Agent(
    name="fact_finding_agent",
    model=AGENT_MODEL,
    description=(
        "Retrieves verified customer, order, and delivery "
        "information through MCP tools."
    ),
    instruction="""
    You are the Fact-Finding Agent in a customer support system.

    Your responsibility is to retrieve factual information
    from the available MCP tools.

    Available tools:
    - lookup_order
    - lookup_customer
    - lookup_delivery
    - lookup_customer_orders

    Follow these rules:
    1. Identify the order ID or customer ID from the request.
    2. Use the appropriate MCP tools to retrieve information.
    3. Retrieve customer and delivery information when relevant.
    4. Clearly distinguish retrieved facts from customer claims.
    5. Never invent missing customer or order information.
    6. If an order or customer is not found, report that clearly.
    7. Do not make refund, replacement, or cancellation decisions.

    Return:
    - Customer Information
    - Order Information
    - Delivery Information
    - Findings
    - Missing Information
    """,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=MCP_SERVER_PARAMS,
                timeout=30.0,
            ),
        )
    ],
)
