# -*- coding: utf-8 -*-
"""
Day 3 - CampusKart AI Assistant
Drive Ready - AI Agents | One Person Company (OPC) Initiative

This adapts the supplied Day 3 reference to CampusKart and uses
Google Gemini through LangChain.
"""

import csv
import os

# Install before running:
# pip install -U langchain-google-genai langchain-core langchain

# In Google Colab, add GOOGLE_API_KEY in the Secrets panel.
# Locally, set GOOGLE_API_KEY as an environment variable.
try:
    from google.colab import userdata
    colab_key = userdata.get("GOOGLE_API_KEY")
    if colab_key:
        os.environ["GOOGLE_API_KEY"] = colab_key
except Exception:
    pass

if not os.environ.get("GOOGLE_API_KEY"):
    raise EnvironmentError(
        "GOOGLE_API_KEY is missing. Add it to Colab Secrets or set it "
        "as an environment variable."
    )

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

# The reference file specifies this model name.
# If it is not available to your API key, replace it with a Gemini
# model currently enabled in your Google AI Studio account.
MODEL_NAME = "gemini-3.8-flash"

llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0.2)

SYSTEM = """
ROLE:
You are the friendly customer-support assistant for CampusKart,
a stationery store serving college students.

BUSINESS FACTS:
- Notebook: Rs 60 each
- Blue pen: Rs 10 each
- Pencil: Rs 5 each
- Geometry box: Rs 120 each
- College record book: Rs 80 each

RULES:
- Never invent prices, stock availability, discounts, or delivery details.
- If information is not included in the business facts, say:
  "I'll check with the store owner."
- Work out totals carefully.
- Ask a short follow-up question if an order is missing important details.

FORMAT:
- Keep replies under 50 words.
- Be friendly and clear.
- Reply in English or Telugu, matching the customer's language.
"""

# Prompt template, conversation history, and chain
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])

chain = prompt | llm | StrOutputParser()
history = []


def ask(question: str) -> str:
    """Ask the CampusKart assistant and retain conversation history."""
    answer = chain.invoke({"history": history, "question": question})
    history.extend([("human", question), ("ai", answer)])
    return answer


def conversation_demo() -> None:
    """Demonstrate customer support and conversation memory."""
    history.clear()
    print("\n--- CampusKart conversation demo ---")
    print("Assistant:", ask(
        "Hi, I'm Hasini. What is the price of a notebook?"
    ))
    print("Assistant:", ask("What is my name?"))


# CSV-based automated tests
def create_sample_test_file(path: str = "test.csv") -> None:
    """Create sample test cases if the CSV file does not exist."""
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["question", "must_include"]
            )
            writer.writeheader()
            writer.writerow({
                "question": "What is the price of a notebook?",
                "must_include": "60",
            })
            writer.writerow({
                "question": "What is the price of a geometry box?",
                "must_include": "120",
            })


def run_tests(path: str = "test.csv") -> None:
    """Run CSV questions against the chain and check expected text."""
    if not os.path.exists(path):
        create_sample_test_file(path)

    with open(path, "r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No test cases found in", path)
        return

    passed = 0
    print("\n--- Automated response tests ---")

    for row in rows:
        question = row["question"]
        expected = row["must_include"]

        try:
            answer = chain.invoke({"history": [], "question": question})
            ok = expected.casefold() in answer.casefold()
            if ok:
                passed += 1
            print(
                ("PASS" if ok else "FAIL"),
                "|", question, "->", answer[:100]
            )
        except Exception as error:
            print("ERROR |", question, "->", str(error))

    print(f"\n{passed}/{len(rows)} tests passed ({passed / len(rows):.0%})")


# LangChain agent demonstration. No tools are attached in this task,
# matching the supplied reference; tools are introduced in a later task.
def agent_demo() -> None:
    from langchain.agents import create_agent

    agent = create_agent(model=llm, tools=[], system_prompt=SYSTEM)
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "Do you have a laptop charger in stock?"
        }]
    })

    print("\n--- Agent demo ---")
    print(result["messages"][-1].content)


def main() -> None:
    print("CampusKart - Gemini AI Assistant")
    print("Model:", MODEL_NAME)
    conversation_demo()
    create_sample_test_file()
    run_tests()
    agent_demo()


if __name__ == "__main__":
    main()
