# AI Trip Planner

AI-powered travel planning agent that builds day-by-day itineraries using LangGraph tool-calling agents. It combines weather, place search, expense calculation, and currency conversion tools, exposed through a FastAPI backend and Streamlit chat UI.

## Features

- Conversational trip planning in natural language
- LangGraph agent with custom tools for weather, attractions, restaurants, activities, transport, expenses, and currency conversion
- FastAPI REST API (`/query`)
- Streamlit frontend for interactive chat
- Google Places search with Tavily fallback

## Tech Stack

- Python 3.10+
- LangChain / LangGraph
- Groq or OpenAI LLMs
- FastAPI + Uvicorn
- Streamlit
- OpenWeatherMap, Google Places, Tavily, ExchangeRate API

## Project Structure

```text
AI-Trip_Planner/
├── agent/                 # LangGraph agent workflow
├── config/                # LLM provider config
├── prompt_library/        # System prompts
├── tools/                 # LangChain tools
├── utils/                 # API helpers and model loader
├── main.py                # FastAPI backend
├── streamlit_app.py       # Streamlit frontend
├── requirements.txt
├── pyproject.toml
└── .env.name              # Environment variable template
```

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- API keys listed below

## Setup

### 1) Clone and enter the project

```bash
git clone https://github.com/ankpal145/AI-Trip_Planner.git
cd AI-Trip_Planner
```

### 2) Create `.env`

Copy the template and fill in your keys:

```bash
copy .env.name .env
```

Required / recommended variables:

```env
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
GPLACES_API_KEY=your_google_places_key
TAVILY_API_KEY=your_tavily_key
OPENWEATHERMAP_API_KEY=your_openweather_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_key
```

Notes:
- At least `GROQ_API_KEY` (default provider) or `OPENAI_API_KEY` is required.
- Place search works best with `GPLACES_API_KEY`; otherwise it falls back to `TAVILY_API_KEY`.
- Weather and currency tools need their respective keys.

### 3) Install dependencies

Using uv (recommended):

```bash
uv sync
```

Or using pip + venv:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

## Run the App

Open **two terminals** from the project root.

### Terminal 1 — Backend (FastAPI)

```bash
uv run uvicorn main:app --reload --port 8000
```

Or with activated venv:

```bash
uvicorn main:app --reload --port 8000
```

Health check: [http://localhost:8000/health](http://localhost:8000/health)

### Terminal 2 — Frontend (Streamlit)

```bash
uv run streamlit run streamlit_app.py
```

Or:

```bash
streamlit run streamlit_app.py
```

Open the Streamlit URL shown in the terminal (usually [http://localhost:8501](http://localhost:8501)).

## Example Query

```text
Plan a trip to Goa for 5 days
```

## API Usage

```bash
curl -X POST http://localhost:8000/query ^
  -H "Content-Type: application/json" ^
  -d "{\"question\": \"Plan a 3-day trip to Manali\"}"
```

## Configuration

LLM settings live in `config/config.yaml`:

```yaml
llm:
  openai:
    provider: "openai"
    model_name: "gpt-4o-mini"
  groq:
    provider: "groq"
    model_name: "llama-3.3-70b-versatile"
```

Default provider in `main.py` is `groq`.

## Troubleshooting

- **Could not connect to the backend**: start FastAPI on port 8000 first.
- **GROQ_API_KEY is missing**: add the key to `.env` and restart the servers.
- **Place/weather/currency tools return unavailable**: add the matching API keys in `.env`.
- **Dependency install fails**: run `uv sync` from the project root (not from nested folders).

## License

See `LICENSE`.
