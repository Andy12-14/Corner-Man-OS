Corner Man OS 🥊
"Everything a fan needs in their corner."
Overview

Purpose: A boxing-focused multi-agent system designed to automate the life of a boxing fan. Just like a corner man handles the water, strategy, and cuts for a fighter, Corner Man OS handles the stats, schedules, and news for the fan.

Scope: This project orchestrates three specialized AI agents to scrape data, track fight schedules, and deliver curated news via WhatsApp.

Tech Stack: Python 3.10+, Google Gemini (LLM), ScrapeGraphAI, DuckDuckGo Search (DDGS), PyWhatKit (WhatsApp automation), APScheduler.

🏗️ Project Structure
workflow2/

main.py : The Ring General. The central orchestrator that runs the agents.

call_functions.py : The Utility Belt. Helper functions for I/O and tool management.

Tools/tools.py : The Toolkit. Contains the specific Python functions (tools) the agents use.

headhunter.py : Agent 1 (The Profiler). Finds stats and highlights.

smoke_detector.py : Agent 2 (The Scout). Finds upcoming fights and sets reminders.

The_plug.py : Agent 3 (The Source). Delivers news and updates.

requirements.txt : List of all dependencies.

🤖 The Agents (The Crew)
1. The Headhunter 🕵️‍♂️
"I find the tape, you watch the knockout."

Role: The Profiler.

Goal: Build comprehensive profiles on boxers.

Capabilities:

Scrapes BoxRec for official records (W-L-D, KOs, titles).

Searches YouTube for career highlights.

Retrives profile images.

Tools: boxer_info, highlights_finder, get_boxer_image.

2. The Smoke Detector 🚨
"Where there's smoke, there's a fight."

Role: The Event Scout.

Goal: Detect upcoming "smoke" (big fights) and ensure you never miss one.

Capabilities:

Scrapes Box.live for the nearest 5 upcoming fights.

Checks for community predictions.

Scheduler: Can set a WhatsApp reminder for the day before a specific fight.

Tools: get_fights, set_reminder.

3. The Plug 🔌
"Everybody knows the Plug got the goods."

Role: The News Connector.

Goal: Curate and deliver the latest boxing news.

Capabilities:

Scrapes ESPN Boxing for the latest headlines and summaries.

Pushes updates directly to your phone via WhatsApp.

Tools: get_news, sent_whatsapp.

🛠️ Installation & Setup
Prerequisites:

Python 3.10+

Chrome Browser (logged into WhatsApp Web)

API Keys: Google Gemini, ScrapeGraphAI.

Step-by-Step Guide:

Clone & Environment:

Bash

# Navigate to project
cd C:/Users/andys/Desktop/AI_agent_boxe/workflow2

# Create virtual environment
python -m venv .venv

# Activate (Windows Bash)
source .venv/Scripts/activate
# Or PowerShell: .venv\Scripts\Activate.ps1
Install Dependencies:

Bash

pip install -r requirements.txt
Key Libraries: os, sys, dotenv, google-genai, scrapegraph-py, duckduckgo-search (ddgs), pywhatkit, apscheduler, requests, datetime, time.

Configuration (.env): Create a .env file in the root directory and add your keys:

Extrait de code

SCRAPEGRAPH_API_KEY=your_key_here
Gemini_API_KEY=your_key_here
🚀 How to Run
1. The Full Experience: Run the main orchestrator to interact with the agents naturally.

Bash

python main.py "Who is Shakur Stevenson?"
2. Specific Agent Tasks: You can trigger specific workflows by passing prompts:

"Get me the latest news and send it to WhatsApp" (Triggers The Plug)

"Find upcoming fights and set a reminder for the Haney fight" (Triggers Smoke Detector)

⚠️ Important Notes
WhatsApp Automation: pywhatkit relies on browser automation. When sending a message, do not touch your mouse or keyboard while the script opens the browser tab.

Scheduling: The set_reminder function puts the script into a "wait" mode. The terminal must remain open for the reminder to fire.

API Credits: ScrapeGraphAI and Gemini have usage limits. Monitor your token usage in the dashboard.

📈 Axis of Improvement & Roadmap
1. Dockerization (The "Gym" Container)
To make Corner Man OS portable and runnable on any server (like a VPS or cloud instance), the next major step is containerization using Docker.

The Goal: Create a Dockerfile so the entire crew (agents + orchestrator) runs with a single command: docker-compose up.

The Challenge (Headless Mode):

Current Issue: pywhatkit opens a visible Chrome browser window to send messages. Docker containers are "headless" (no screen), so pywhatkit will crash.

Solution A (The Hack): Install Xvfb (virtual display) inside the Docker container to trick the script into thinking there is a screen.

Solution B (The Pro Move): Replace pywhatkit with the Official WhatsApp Business API or Twilio API. This allows the agents to run silently in the background without needing a browser, making the system 100% cloud-ready.

2. The "Ringside" Dashboard (Flask UI)
Currently, the agents communicate via the terminal. The next version will feature a web-based User Interface (UI) using Flask.

Why Flask? It’s a lightweight Python web framework that integrates easily with our existing scripts.

Planned Features:

Dashboard: A simple webpage displaying upcoming fights found by the Smoke Detector.

Search Bar: A text box to query the Headhunter (e.g., "Gervonta Davis stats") and see the profile card on screen.

Control Panel: Buttons to manually trigger "News Fetch" or "Set Reminder" without typing commands.

Architecture:

app.py: Serves the HTML frontend.

background_worker: Runs the APScheduler independently so reminders still fire even if the webpage isn't open.

3. Database Integration (The Record Book)
Current State: Data is printed or lost when the script ends.

Improvement: Connect a simple database (like SQLite or PostgreSQL) to store:

Boxer profiles (so we don't scrape BoxRec every time).

User stats (favorite fighters, betting history).

Past fight results and prediction accuracy.

Maintainer: Andy

Course: Coding for AI & Data Science

Repo: Debugger_agent
