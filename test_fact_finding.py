import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from customer_support_agent.agents.fact_finding_agent import fact_finding_agent


async def main():
    session_service = InMemorySessionService()

    runner = Runner(
        agent=fact_finding_agent,
        app_name="customer_support_test",
        session_service=session_service,
    )

    await session_service.create_session(
        app_name="customer_support_test",
        user_id="test_user",
        session_id="test_session",
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text="Find the order details for ORD1001.")],
    )

    async for event in runner.run_async(
        user_id="test_user",
        session_id="test_session",
        new_message=message,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text)


if __name__ == "__main__":
    asyncio.run(main())