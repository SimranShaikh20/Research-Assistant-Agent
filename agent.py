"""
Research Assistant Agent — Built with Google ADK
================================================
A multi-step agent that searches the web, summarizes findings,
and suggests follow-up questions. Built for the Google Cloud NEXT '26
Writing Challenge on DEV Community.

Author: [Your Name]
GitHub: [Your GitHub URL]
"""

from google.adk.agents import Agent
from google.adk.tools import google_search


# ─────────────────────────────────────────────
# Sub-Agent 1: Web Searcher
# Responsibility: Hit the web, return raw findings
# ─────────────────────────────────────────────
searcher_agent = Agent(
    name="web_searcher",
    model="gemini-2.0-flash",
    description="Searches the web for up-to-date information on a given topic.",
    instruction="""
    You are a web research specialist. Your only job is to search for 
    accurate, recent information on the topic given to you.

    Rules:
    - Always use the google_search tool — never answer from memory alone
    - Prioritize sources from 2025-2026
    - Return a clear summary of what you found, including source context
    - If results are conflicting, mention both sides
    - Keep it factual, no opinions
    """,
    tools=[google_search],
)


# ─────────────────────────────────────────────
# Sub-Agent 2: Summarizer & Analyst
# Responsibility: Turn raw findings into structured insight
# ─────────────────────────────────────────────
summarizer_agent = Agent(
    name="analyst_summarizer",
    model="gemini-2.0-flash",
    description="Structures raw research into clear developer-friendly summaries.",
    instruction="""
    You are a technical writer for a developer audience.
    You receive raw research findings and turn them into:

    ## 🔍 Key Findings
    [3-4 bullet points of the most important facts]

    ## 💡 The Most Surprising Thing
    [One insight that might be unexpected or counterintuitive]

    ## ⚠️ What to Watch Out For
    [Any caveats, limitations, or things that could go wrong]

    ## ❓ Go Deeper: 3 Follow-Up Questions
    [Three specific questions a developer might want to explore next]

    Keep the tone honest, direct, and useful. No marketing fluff.
    """,
)


# ─────────────────────────────────────────────
# Root Agent: Coordinator
# Responsibility: Orchestrate the full research pipeline
# ─────────────────────────────────────────────
root_agent = Agent(
    name="research_coordinator",
    model="gemini-2.0-flash",
    description="Coordinates multi-step research by delegating to specialist sub-agents.",
    instruction="""
    You are a research coordinator managing a two-step pipeline:

    Step 1 — Delegate to web_searcher to find current information on the topic.
    Step 2 — Pass those findings to analyst_summarizer to structure them clearly.
    Step 3 — Present the final structured output to the user.

    Always complete both steps before responding. Do not skip the search step.
    If the user's query is vague, make a reasonable assumption and state it clearly.

    Start your final response with:
    "Here's what I found after searching the web:"
    """,
    agents=[searcher_agent, summarizer_agent],
)
