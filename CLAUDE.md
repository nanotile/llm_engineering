# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LLM Engineering course repository - an 8-week curriculum progressing from basic LLM interactions to autonomous agentic AI solutions.

## Development Commands

**All commands run from `llm_engineering/` directory:**

```bash
# Run Python scripts
uv run python week8/deal_agent_framework.py

# Add dependencies
uv add <package>

# Sync environment
uv sync

# Run Gradio apps (week5)
uv run python week5/app.py        # RAG chatbot
uv run python week5/evaluator.py  # Evaluation dashboard

# Run Modal deployments (week7) - requires `modal setup` first
uv run modal deploy week8/pricer_service.py
```

**Jupyter notebooks**: Use `.venv` kernel in Cursor/VS Code.

**Environment**: Python 3.12, API keys in `llm_engineering/.env`

## Architecture: Week 8 Agent Framework

The deal discovery system uses a multi-agent pipeline orchestrated by `DealAgentFramework`:

```
DealAgentFramework.run()
    └── PlanningAgent.plan()
            ├── ScannerAgent.scan()      # Scrapes RSS feeds for deals
            ├── EnsembleAgent.price()    # Estimates product value
            │       ├── FrontierAgent    # GPT/Claude price estimation
            │       └── NeuralNetworkAgent # ML model estimation
            └── MessagingAgent.alert()   # Sends notifications
```

- `agents/deals.py` - Data models (ScrapedDeal, Deal, Opportunity)
- `agents/scanner_agent.py` - RSS feed parsing with LLM extraction
- `agents/frontier_agent.py` - Uses GPT-4 for price estimation
- `agents/ensemble_agent.py` - Combines multiple estimation strategies
- `memory.json` - Persists discovered opportunities across runs

## Architecture: Week 5 RAG System

```
knowledge-base/ → ingest.py → ChromaDB vectorstore
                                    ↓
                              answer.py ← user query
                                    ↓
                              app.py (Gradio UI)
```

- `evaluation/eval.py` - Runs retrieval and answer quality tests against `tests.jsonl`

## Key Files by Module

| Week | Key Entry Points |
|------|------------------|
| 5 | `app.py`, `evaluator.py`, `implementation/ingest.py`, `implementation/answer.py` |
| 7 | `pricer/` for Modal training, `util.py` for data prep |
| 8 | `deal_agent_framework.py`, `agents/planning_agent.py` |

## Free API Alternatives

See `guides/09_ai_apis_and_ollama.ipynb` for Ollama, Gemini, and OpenRouter as free alternatives to paid APIs.
