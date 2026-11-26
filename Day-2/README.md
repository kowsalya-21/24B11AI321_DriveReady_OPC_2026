# Day 2 - Sweet Crumbs Home Bakery AI Assistant

## Business idea
Sweet Crumbs is a small home bakery that sells plum cakes, chocolate cakes, and cupcakes. This project adapts the Day 2 AI-agent exercises to a bakery customer-support use case.

## Sample product catalogue

| Product | Price |
|---|---:|
| Plum cake | Rs. 500 |
| Chocolate cake | Rs. 650 |
| Cupcake | Rs. 80 |

Business rules:
- Orders require at least 24 hours' notice.
- Eggless versions are available for cakes.
- The assistant must not invent prices or promise delivery times.
- Unknown information should be referred to the owner.

## Concepts demonstrated
- Business-specific system prompts
- Groq LLM integration
- Product catalogue and price calculation function
- Conversation memory
- API rate-limit and connection error handling
- Customer message classification (order, question, complaint)
- Order detail extraction into JSON
- Prompt safety demonstration using Groq Prompt Guard

## Setup

1. Install Python 3.10 or later.
2. Install the required packages:

   ```bash
   pip install groq
   ```

3. Set your Groq API key as an environment variable.

   **Windows PowerShell:**
   ```powershell
   $env:GROQ_API_KEY="your_groq_api_key"
   ```

   **macOS / Linux:**
   ```bash
   export GROQ_API_KEY="your_groq_api_key"
   ```

4. Run the program:

   ```bash
   python task.py
   ```

5. Choose `1` to run the demonstrations or `2` to start the customer chat.

## Security
Do not paste your real API key into this file or commit it to the public GitHub repository. Keep it in an environment variable or a secrets manager.
