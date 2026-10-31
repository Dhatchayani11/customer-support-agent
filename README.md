# AI-Powered Customer Support Agent

## Project Overview

An AI-powered multi-agent customer support system designed to automate customer service operations through intelligent query understanding, specialized agent collaboration, tool integration, and structured response generation.

The system uses Google's Agent Development Kit (ADK) to coordinate multiple specialized AI agents. Each agent is responsible for a specific customer support task, enabling modular, scalable, and maintainable workflows.

## Business Problem

Traditional customer support systems often depend on manual investigation, predefined responses, and multiple interactions to resolve customer issues.

This project aims to improve that process by introducing an agent-based architecture that can:

- Understand customer queries.
- Identify customer intents.
- Retrieve order and customer information.
- Investigate delivery-related complaints.
- Retrieve relevant knowledge.
- Analyze customer cases.
- Prepare appropriate resolutions.

## Key Features

- Multi-agent orchestration.
- Intent-based query routing.
- Specialized agents for customer support operations.
- Order and customer information retrieval.
- Delivery investigation.
- Knowledge retrieval.
- Case analysis and resolution preparation.
- MCP-based tool integration.
- Context-aware customer interactions.
- Structured response generation.

## Architecture

The application follows a multi-agent architecture consisting of a root orchestrator and four specialized agents.

### Agents

| Agent               | Responsibility                                                        |
| ------------------- | --------------------------------------------------------------------- |
| Orchestrator Agent  | Receives customer queries and coordinates the workflow.               |
| Fact-Finding Agent  | Retrieves order, customer, and delivery information.                  |
| Knowledge Agent     | Retrieves relevant knowledge for customer support queries.            |
| Case Analysis Agent | Analyzes the collected information and identifies the customer issue. |
| Resolution Agent    | Prepares an appropriate resolution based on the investigation.        |

## Technology Stack

| Technology   | Purpose                               |
| ------------ | ------------------------------------- |
| Python       | Primary programming language          |
| Google ADK   | Agent development and orchestration   |
| Groq         | LLM inference provider                |
| GPT-OSS-120B | Model used in standalone Groq testing |
| MCP          | Standardized tool integration         |
| JSON         | Local structured data storage         |
| LiteLLM      | LLM provider integration              |

## MCP Integration

The project includes a standalone MCP server and client.

The MCP server exposes the following tools:

- `lookup_order`
- `lookup_customer`
- `lookup_delivery`
- `lookup_customer_orders`

These tools support order lookup, customer information retrieval, delivery information retrieval, and customer order history retrieval.

The standalone MCP server and client have been tested independently. Integration with the ADK Fact-Finding Agent remains subject to end-to-end validation.

## Project Structure

```text
customer-support-agent/
│
├── README.md
│
├── docs/
│   ├── architecture.md
│   ├── agent_workflow.md
│   ├── testing.md
│   └── setup_guide.md
│
├── agents/
│   ├── orchestrator.py
│   ├── fact_finding_agent.py
│   ├── knowledge_agent.py
│   ├── case_analysis_agent.py
│   └── resolution_agent.py
│
├── tools/
│
├── mcp_server/
│
├── tests/
│
├── requirements.txt
├── .env.example
└── .gitignore
```

Note: The structure above represents the logical organization. Update filenames and folders to match the actual repository.

## Getting Started

### Prerequisites

- Python 3.10 or a version supported by your installed ADK release.
- Google ADK.
- Groq API key.
- Required Python dependencies.
- MCP-compatible development environment.

### Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd customer-support-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install required dependencies.

Configure the required environment variables using `.env.example` as a reference.

### Running the Application

Use the execution command corresponding to the actual ADK entry point and project structure.

For a standard ADK project, the development interface can be started using:

```bash
adk web
```

Run the MCP server separately when testing its standalone functionality.

## Sample Customer Queries

**Order lookup**

```text
Where is my order ORD1002?
```

**Delivery complaint**

```text
My order was marked delivered, but I haven't received it.
```

**Customer order history**

```text
Can you show me my recent orders?
```

## Future Enhancements

- Complete ADK and MCP integration.
- Improve tool-calling reliability.
- Expand customer support scenarios.
- Add comprehensive automated testing.
- Introduce persistent conversation state where required.
- Improve monitoring and error handling.

## Disclaimer

This project is a learning and portfolio implementation of an AI-powered customer support system. It is not a production-ready customer support platform.
