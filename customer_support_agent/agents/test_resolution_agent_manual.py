import asyncio
from pathlib import Path
from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parents[2]
PACKAGE_DIR = Path(__file__).resolve().parents[1]

package_env = PACKAGE_DIR / ".env"
root_env = PROJECT_DIR / ".env"

if package_env.exists():
    load_dotenv(package_env)
elif root_env.exists():
    load_dotenv(root_env)
else:
    raise FileNotFoundError("Could not find the project's .env file")

from .resolution_agent import resolution_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types



async def main():
    session_service = InMemorySessionService()

    runner = Runner(
        agent=resolution_agent,
        app_name="resolution_test",
        session_service=session_service,
    )

    user_id = "test_user"
    session_id = "resolution_session"

    await session_service.create_session(
        app_name="resolution_test",
        user_id=user_id,
        session_id=session_id,
    )

    case_assessment = """
    Case Overview
    Order ORD1001: Package marked delivered but not received.

    Verified Facts
    Order status: Delivered.
    Delivery status: Delivered.
    Delivery date: 2026-10-27.
    Proof of delivery: Photo available.
    Delivery notes: Package left at the front door.

    Customer-Reported Claims
    Customer states that the package was not received.

    Relevant Policy Evidence
    Delivery policy retrieved. Further eligibility verification required.

    Evidence Comparison
    Delivery records indicate delivery, but they do not establish
    that the customer personally received the package.

    Missing Information and Risks
    Customer receipt is unverified. Photo contents have not been reviewed.

    Recommended Next Investigation Step
    Verify the delivery photo and investigate the delivery location.
    """

    message = (
        "Prepare resolution options for this case assessment. "
        "Do not assume the customer is eligible for a refund.\n\n"
        + case_assessment
    )

    response = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text=message)],
        ),
    )

    for event in response:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text)


if __name__ == "__main__":
    asyncio.run(main())