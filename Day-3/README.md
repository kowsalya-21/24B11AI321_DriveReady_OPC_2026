# Day 3 - CampusKart AI Assistant

**Drive Ready - AI Agents | One Person Company (OPC) Initiative**

## Objective

Adapt the supplied Day 3 reference to CampusKart, a stationery store serving college students, and use Google Gemini through LangChain.

## Business use case: CampusKart

| Product | Price |
|---|---:|
| Notebook | ₹60 |
| Blue pen | ₹10 |
| Pencil | ₹5 |
| Geometry box | ₹120 |
| College record book | ₹80 |

The assistant must not invent stock, discounts, or delivery details. For information not provided, it says: **"I'll check with the store owner."**

## Concepts implemented

1. Gemini API integration using `ChatGoogleGenerativeAI`.
2. Business-specific system prompt.
3. Prompt template using `ChatPromptTemplate`.
4. Conversation memory using `MessagesPlaceholder` and chat history.
5. Output parsing using `StrOutputParser`.
6. CSV-based response testing using `run_tests()`.
7. LangChain agent creation using `create_agent` with an empty tools list, matching the supplied reference.

## Files

```text
Day-3/
├── task.py
└── README.md
```

The program creates `test.csv` automatically if it is not present. This is runtime test data, not an additional required submission file.

## Setup and execution

### 1. Install dependencies

```bash
pip install -U langchain-google-genai langchain-core langchain
```

### 2. Configure the Gemini API key

**Google Colab**
1. Open the Secrets panel (key icon).
2. Add a secret named `GOOGLE_API_KEY`.
3. Paste your Gemini API key as its value.
4. Allow the notebook to access the secret.

**Local computer**

Set `GOOGLE_API_KEY` as an environment variable before running the program. Do not paste the key directly into `task.py`.

### 3. Run

```bash
python task.py
```

The program demonstrates a customer conversation, runs the CSV-based tests, and creates a LangChain agent.

## Model note

The supplied reference specifies `gemini-3.8-flash`, so that model name is retained in `task.py`. Model availability depends on the Google API access associated with your key. If the API reports that the model is unavailable, replace `MODEL_NAME` with a Gemini model currently enabled in your Google AI Studio account.

## Security

- Never commit your Gemini API key to GitHub.
- Do not upload `.env` files containing secrets.
- Use Colab Secrets or an environment variable for the key.
