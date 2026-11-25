# Day 1 - AI Agents

## Overview
This task demonstrates how to connect a Groq-hosted language model using LangChain, provide it with system instructions, and test a prompt-safety model.

## Concepts covered
- Connecting to Groq with `langchain-groq`
- Reading the API key from an environment variable
- Initializing `ChatGroq`
- Using system and human messages
- Creating a reusable `ask()` function
- Testing the Groq Prompt Guard model

## Files
- `task.py` - Python source code for the Day 1 exercise
- `requirements.txt` - Python dependencies

## Setup

1. Install Python 3.10 or later.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
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

4. Run:

   ```bash
   python task.py
   ```

## Important
Never commit your real API key, passwords, or other secrets to this public repository.
