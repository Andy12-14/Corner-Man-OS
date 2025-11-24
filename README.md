# Corner Man OS 🥊

### *"Everything a fan needs in their corner."*

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
