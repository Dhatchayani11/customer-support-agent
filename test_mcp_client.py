
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "customer_support_agent.mcp_server"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\nMCP server connected successfully!")

            tools = await session.list_tools()

            print("\nAvailable MCP tools:")

            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            print("\nTesting order lookup:")

            result = await session.call_tool(
                "lookup_order",
                {"order_id": "ORD1001"},
            )

            for content in result.content:
                if content.type == "text":
                    print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
