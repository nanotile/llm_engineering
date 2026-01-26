# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the LLM Engineering course repository - an 8-week educational curriculum for learning AI and LLM development. The course progresses from basic LLM interactions to building autonomous agentic AI solutions.

## Development Environment

**Package Manager**: uv (not pip or conda)
- Install packages: `uv add <package>`
- Run scripts: `uv run python <script.py>`
- Sync dependencies: `uv sync`

**Python Version**: 3.12 (specified in `.python-version`)

**Environment Variables**: Store API keys in `.env` file in `llm_engineering/` directory:
```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=...
```

## Running Code

Run Jupyter notebooks in Cursor/VS Code with the `.venv` kernel selected.

Run Python scripts:
```bash
cd llm_engineering
uv run python week8/deal_agent_framework.py
```

Run Gradio apps:
```bash
cd llm_engineering/week5
uv run python app.py        # RAG chatbot
uv run python evaluator.py  # Evaluation dashboard
```

## Repository Structure

- `llm_engineering/` - Main course content
  - `week1-week8/` - Progressive course modules with daily notebooks (`day1.ipynb`, etc.)
  - `guides/` - Foundational guides (Python, notebooks, APIs, debugging)
  - `setup/` - Platform-specific setup instructions
  - `community-contributions/` - Student projects and solutions

## Course Architecture by Week

- **Week 1-2**: LLM API fundamentals (OpenAI, Anthropic), prompting, web scraping
- **Week 3**: Google Colab, GPU computing, transformers
- **Week 4**: Code generation and analysis tools
- **Week 5**: RAG systems with ChromaDB and LangChain
  - `implementation/` - RAG answer generation
  - `evaluation/` - Retrieval/answer quality metrics
- **Week 6**: Fine-tuning LLMs, JSONL data formats
- **Week 7**: Model training on Modal cloud platform
- **Week 8**: Agentic AI framework
  - `agents/` - Modular agent architecture (planning, scanning, frontier, ensemble agents)
  - `deal_agent_framework.py` - Orchestrates multi-agent product deal discovery

## Key Dependencies

- **LLM APIs**: openai, anthropic, google-generativeai, ollama
- **LangChain ecosystem**: langchain, langchain-openai, langchain-chroma
- **ML/Data**: torch, transformers, scikit-learn, pandas, numpy
- **Vector DB**: chromadb
- **UI**: gradio
- **Cloud**: modal

## Free API Alternatives

See `guides/09_ai_apis_and_ollama.ipynb` for using Ollama, Gemini, and OpenRouter as free alternatives to paid APIs.
