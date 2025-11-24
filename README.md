<<<<<<< HEAD
  - `headhunter.py`     : Boxing-specific agent that finds and builds boxer profiles.
  - `smoke_detector.py` : Boxing-specific agent that finds "smoke" fights (slang for hot/upcoming fights) and can schedule reminders.
  - `The_plug.py`       : Boxing news agent that pushes curated boxing news to WhatsApp (the "plug" / source connector).
  - `pyproject.toml` / `requirements.txt` : Dependency files; use the `workflow2/requirements.txt` if present.
  - `test.py` / `test`  : Quick test scripts or examples for manual validation.
  - `agents/` and `Tools/` : helper modules used by the agents (if present).

Boxing-specific agent descriptions
- `headhunter` (boxer profiler):
  - Goal: locate and build boxer profiles. It uses sources such as BoxRec (official records), YouTube highlights, and public images to compile a profile for a boxer.
  - Outputs: a structured boxer profile (name, record, weight class, BoxRec URL/ID, notable highlights links, thumbnail image URL or saved image path, basic stats and short biography).
  - Typical flow: search BoxRec or other boxing databases → collect official record and metadata → find latest or best YouTube highlights and pull video links → attempt to find a representative image → normalize into a `profile` object for other agents.

- `smoke_detector` (fight finder & reminder):
  - Goal: detect "smoke" fights — slang for notable or upcoming fights — from web sources, social media, or feeds.
  - Capabilities:
    - Find and surface upcoming fights using keywords, RSS, or scraping.
    - Interpret slang/mentions (e.g., "smoke", "banger", "must-see") to prioritize events.
    - Schedule WhatsApp reminders for a precise date/time (day, hour, minute) to notify users.
  - Integration note: to send WhatsApp reminders you must configure a messaging gateway (e.g., Twilio WhatsApp, WhatsApp Business API, or a community library that supports scheduled messages) and provide credentials in `config.py` or environment variables.

- `The_plug` (boxing news & notifications):
  - Goal: act as the news/source connector (the "plug") that pushes curated boxing news to a WhatsApp number or group.
  - Capabilities:
    - Aggregate boxing news (headlines, short summaries, links).
    - Send updates via WhatsApp as short messages or digests.
    - Optionally accept filters (fighters, events, keywords) to tailor the feed.
  - Integration note: same as `smoke_detector` for WhatsApp — ensure credentials and target numbers/groups are configured.

Role of `main.py`
- `main.py` is the orchestrator for `workflow2`. Typical responsibilities:
  - Load configuration (from `config.py` or environment variables) including messaging credentials.
  - Instantiate and run the three agents (either sequentially or concurrently).
  - Route data: e.g., use `headhunter` to build boxer profiles → `smoke_detector` to find fights and schedule reminders → `The_plug` to push news and highlights.
  - Offer a CLI for single-run demo or a long-running service mode.

Installation & Virtual Environment (bash on Windows)
Prereqs:
  - Python 3.10+ (recommended). Ensure `python` points to the intended interpreter.

Step-by-step (run from project root `C:/Users/andys/Desktop/AI_agent_boxe`):

1) Create a venv (project-local)
```bash
python -m venv .venv
```

2) Activate the venv (bash.exe / Git Bash)
```bash
source .venv/Scripts/activate
```
If you use PowerShell, run:
```powershell
.venv\\Scripts\\Activate.ps1
```

3) Install dependencies for `workflow2` (recommended to cd into `workflow2` first)
```bash
cd workflow2
pip install -r requirements.txt
```

4) Confirm installation
```bash
python -c "import sys; print(sys.executable); print(sys.version)"
```

WhatsApp / Messaging setup (required for reminders and news)
  - The `smoke_detector` and `The_plug` agents require a messaging gateway to send WhatsApp messages. Options include:
    - Twilio WhatsApp API (recommended for production).
    - WhatsApp Business API.
    - Community wrappers or `yowsup`-style tools (less reliable / unsupported).
  - Provide credentials (API keys, phone IDs, webhook URLs) via `config.py` or environment variables. Example env vars to set:
    - `WHATSAPP_API_KEY`, `WHATSAPP_FROM`, `WHATSAPP_TO`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`.
  - Scheduling reminders: `smoke_detector` will accept a target date/time (day, hour, minute) and create a scheduled send via the configured gateway. For reliable scheduling, run `main.py` as a persistent service or configure a separate scheduler (cron, APScheduler).

Running the project
  - From within `workflow2` (after activating venv):
```bash
python main.py
```
  - For a demo run, inspect `test.py` or add a `--demo` flag to `main.py` to run a short pipeline: build a boxer profile, find a smoke fight, and send a test WhatsApp message.

Developer notes & conventions
  - Config: Use `config.py` or environment variables for API keys and phone numbers. Do not commit secrets.
  - Logging: Use Python's `logging` module and set levels via `main.py`.
  - Tests: Add `pytest` tests for each agent. Use mocks for external HTTP and messaging calls.
  - Data: If `headhunter` downloads images or videos, store them in a `data/` subfolder and keep filenames consistent (e.g., `{boxer_slug}.jpg`).

Troubleshooting
  - WhatsApp/Message sending fails: verify API credentials, phone numbers, and gateway configuration. Check gateway logs.
  - Scheduling issues: ensure `main.py` or a scheduler is running at the scheduled time; local clocks/timezones must match the intended target time.

Suggested next steps
  - Add a `README.md` (markdown) for GitHub rendering.
  - Add a demo mode in `main.py` that performs: `headhunter` → `smoke_detector` (schedule) → `The_plug` (send news).
  - Add unit tests and CI that mocks messaging gateways.

Contact / Maintainer
  - Maintainer: Andy (local workspace owner)
  - Repo: `Debugger_agent` (branch `main`)
=======
# Corner Man OS 🥊

### *"Everything a fan needs in their corner."*
>>>>>>> dd9eac6a95df4bfcd0fbf1a84d22a2ce21615884

---

## 📖 Overview

**Corner Man OS** is a boxing-focused Multi-Agent System (MAS) designed to automate the life of a fight fan. Just like a professional corner man handles the water, strategy, and cut-work for a fighter, **Corner Man OS** handles the statistics, scheduling, and news for the user.

It orchestrates three specialized AI agents to scrape official records, track upcoming fight schedules, and deliver curated news updates directly via WhatsApp.

---

## 🏗️ Tech Stack

* **Language:** Python 3.10+
* **LLM Engine:** Google Gemini (via `google-genai`)
* **Web Scraping:** ScrapeGraphAI (`scrapegraph-py`)
* **Search & Media:** DuckDuckGo Search (`ddgs`), YouTube (via search)
* **Automation:** PyWhatKit (WhatsApp Web automation), APScheduler
* **Core Libraries:** `os`, `sys`, `dotenv`, `requests`, `datetime`, `time`

---

## 🤖 The Agents (The Crew)

The system is built around three distinct agents, each with a specific personality and toolset:

### 1. The Headhunter 🕵️‍♂️
> *"I find the tape, you watch the knockout."*

* **Role:** The Profiler.
* **Goal:** Build comprehensive profiles on specific boxers.
* **Capabilities:**
    * Scrapes BoxRec for official records (W-L-D, KOs, titles).
    * Searches YouTube for career highlights and video clips.
    * Retrieves profile images.
* **Tools:** `boxer_info`, `highlights_finder`, `get_boxer_image`

### 2. The Smoke Detector 🚨
> *"Where there's smoke, there's a fight."*

* **Role:** The Event Scout.
* **Goal:** Detect upcoming "smoke" (big fights) and ensure the user never misses an event.
* **Capabilities:**
    * Scrapes `Box.live` for the nearest 5 upcoming fights.
    * Analyzes community predictions.
    * **Scheduler:** Sets a WhatsApp reminder for the day before a specific fight.
* **Tools:** `get_fights`, `set_reminder`

### 3. The Plug 🔌
> *"Everybody knows the Plug got the goods."*

* **Role:** The News Connector.
* **Goal:** Curate and deliver the latest boxing news immediately.
* **Capabilities:**
    * Scrapes ESPN Boxing for the latest headlines and summaries.
    * Pushes updates directly to the user's phone via WhatsApp.
* **Tools:** `get_news`, `sent_whatsapp`

---

## 📂 Project Structure

```text
workflow2/
├── main.py              # The Ring General (Orchestrator script)
├── call_functions.py    # The Utility Belt (I/O & Helper functions)
├── Tools/
│   └── tools.py         # The Toolkit (Agent function definitions)
├── headhunter.py        # Agent 1 Logic
├── smoke_detector.py    # Agent 2 Logic
├── The_plug.py          # Agent 3 Logic
├── requirements.txt     # Dependency list
└── .env                 # API Keys (Not included in repo)
