# 🤖 ADK Research Assistant Agent



## What It Does

Give it any topic → it searches the web → structures the findings → suggests what to explore next.

Built as a **multi-agent pipeline**:
- `web_searcher` — hits Google Search for fresh info
- `analyst_summarizer` — turns raw results into structured developer-friendly output
- `research_coordinator` — orchestrates the full flow

## Quick Start

### 1. Prerequisites
- Python 3.11 or higher
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com)

### 2. Setup

```bash
# Clone the repo
git clone [YOUR_GITHUB_URL]
cd adk_research_agent

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install ADK
pip install google-adk
```

### 3. Configure API Key

```bash
# Copy the example env file
copy .env.example .env      # Windows
cp .env.example .env        # Mac/Linux

# Open .env and add your Gemini API key
# Get it free from: https://aistudio.google.com
```

### 4. Run the Agent

```bash
# Web UI (recommended — great for seeing agent steps)
adk web research_agent/

# Terminal mode
adk run research_agent/
```

Then open `http://localhost:8000` in your browser.

## Example Prompts to Try

```
"What was announced at Google Cloud NEXT 2026?"
"What is the A2A protocol and why does it matter for developers?"
"What is Google ADK 2.0 and how is it different from 1.x?"
"Explain Gemini Enterprise Agent Platform in plain English"
```

## Project Structure

```
adk_research_agent/
├── research_agent/
│   ├── agent.py        ← all the agent logic lives here
│   └── __init__.py
├── .env.example        ← copy this to .env
├── .gitignore
└── README.md
```

## Built With

- [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models)
- Python 3.11+

## Related Article

Read the full honest walkthrough on DEV Community:
👉 [YOUR DEV.TO ARTICLE LINK HERE]

---

Built for the [Google Cloud NEXT '26 Writing Challenge](https://dev.to/challenges/googlecloudnext) on DEV Community.
