# Day 2 - CampusKart AI Assistant

**Drive Ready - AI Agents | One Person Company (OPC) Initiative**

## Objective

Apply the Day 2 AI-agent concepts to CampusKart, a stationery store serving college students. The assistant supports product-price enquiries, customer conversations, message classification, order extraction, and prompt-safety checking.

## Business use case: CampusKart

| Product | Price |
|---|---:|
| Notebook | ₹60 |
| Blue pen | ₹10 |
| Pencil | ₹5 |
| Geometry box | ₹120 |
| College record book | ₹80 |

The assistant must not invent stock, discounts, or delivery details. If information is unavailable, it says: **"I'll check with the store owner."**

## Concepts implemented

1. Groq API client setup.
2. Business-specific system prompt.
3. Logging decorator for function calls.
4. Product price lookup and quantity-based total calculation.
5. Conversation history with a maximum retained-turn window.
6. API error handling for rate limits and connection failures.
7. Customer-message classification into `order`, `question`, or `complaint`.
8. Structured order extraction into JSON.
9. Prompt-safety demonstration using Prompt Guard.

## Files

```text
Day-2/
├── task.py
└── README.md
```

## Setup and execution

### 1. Install the package

```bash
pip install groq
```

### 2. Configure the Groq API key

In Google Colab, add a secret named `GROQ_API_KEY` and allow notebook access to it.

For local execution, set `GROQ_API_KEY` as an environment variable. Never paste the key directly into this file or commit it to GitHub.

### 3. Run

```bash
python task.py
```

The script demonstrates price lookup, customer chat, classification, JSON order extraction, and prompt safety.

## Model note

The script retains the model names used in the Day 2 exercise: `openai/gpt-oss-120b` and `meta-llama/llama-prompt-guard-2-22m`. Availability depends on your Groq account and current API access. If a model is unavailable, select an available compatible model in your Groq console and update the corresponding constant.

## Security

- Do not upload API keys to GitHub.
- Do not commit `.env` files containing secrets.
- Use Colab Secrets or environment variables.
