# Corner-Man-OS 🥊 — Boxing Intelligence Agents

> A multi-agent AI system for boxing enthusiasts, featuring web scraping, AI-powered insights, and WhatsApp notifications.

[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-andy94500%2Fcorner--man--os-blue)](https://hub.docker.com/r/andy94500/corner-man-os)
[![GitHub](https://img.shields.io/badge/GitHub-Andy12--14%2FCorner--Man--OS-green)](https://github.com/Andy12-14/Corner-Man-OS)

## 🚀 Quick Start

### Option 1: Docker Hub (Fastest - No Clone Required!)

```bash
# 1. Create a .env file with your API keys
cat > .env << EOF
Gemini_API_KEY=your_gemini_api_key_here
SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key_here
EOF

# 2. Pull and run from Docker Hub
docker pull andy94500/corner-man-os:latest
docker run -p 5000:5000 --env-file .env andy94500/corner-man-os:latest

# 3. Open http://localhost:5000 in your browser
```

**Docker Hub:** https://hub.docker.com/r/andy94500/corner-man-os

### Option 2: Clone from GitHub

```bash
git clone https://github.com/Andy12-14/Corner-Man-OS.git
cd Corner-Man-OS/workflow2
# Create .env file (see below)
docker-compose up
```

**GitHub Repository:** https://github.com/Andy12-14/Corner-Man-OS

---

## 📋 Table of Contents

- [Overview](#overview)
- [The Three Agents](#the-three-agents)
- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
  - [Docker (Recommended)](#docker-recommended)
  - [Local Installation](#local-installation-with-whatsapp-support)
- [Usage Guide](#usage-guide)
- [WhatsApp Integration](#whatsapp-integration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Overview

Corner-Man-OS is a boxing-focused multi-agent system with a Flask web interface. The project features three specialized AI agents powered by Google Gemini that help you track boxers, find upcoming fights, and stay updated with boxing news.

### The Three Agents

1. **🎯 Headhunter**
   - Finds and builds comprehensive boxer profiles
   - Scrapes BoxRec for official records and stats
   - Locates YouTube highlights
   - Retrieves boxer images
   - *Catchphrase: "I find everything about everyone."*

2. **🔥 Smoke Detector**
   - Detects "smoke" (slang for fights) - upcoming boxing matches
   - Scrapes box-live for fight schedules
   - Can set WhatsApp reminders for fights (local version only)
   - *Catchphrase: "Where there's smoke, there's a fight!"*

3. **📰 The Plug**
   - Your source for boxing journalism
   - Scrapes ESPN for the latest boxing news
   - Can send news summaries via WhatsApp (local version only)
   - *Catchphrase: "Everybody knows the plug has the goods (;)"*

---

## Prerequisites

### Required API Keys

You **MUST** have both of these API keys to run this project:

1. **Google Gemini API Key** - Powers the AI agents
   - Get it from: https://ai.google.dev/
   - Free tier available
   - Set as: `Gemini_API_KEY` in `.env`

2. **ScrapeGraph API Key** - Enables web scraping
   - Get it from: https://scrapegraphai.com/
   - Required for BoxRec, ESPN, and box-live scraping
   - Set as: `SCRAPEGRAPH_API_KEY` in `.env`

### Create `.env` File

Create a `.env` file in the project root:

```env
Gemini_API_KEY=your_gemini_api_key_here
SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key_here
```

⚠️ **Never commit your `.env` file to Git!** It's already in `.gitignore`.

---

## Installation Methods

### Docker (Recommended)

Docker is the easiest way to run Corner-Man-OS. Choose between pulling from Docker Hub or building from source.

#### Method A: Pull from Docker Hub (Easiest!)

**No need to clone the repository!**

```bash
# 1. Create .env file
cat > .env << EOF
Gemini_API_KEY=your_gemini_api_key_here
SCRAPEGRAPH_API_KEY=your_scrapegraph_api_key_here
EOF

# 2. Pull the image
docker pull andy94500/corner-man-os:latest

# 3. Run the container
docker run -p 5000:5000 --env-file .env andy94500/corner-man-os:latest

# 4. Access at http://localhost:5000
```

**Docker Hub Link:** https://hub.docker.com/r/andy94500/corner-man-os

#### Method B: Build from GitHub Source

```bash
# 1. Clone the repository
git clone https://github.com/Andy12-14/Corner-Man-OS.git
cd Corner-Man-OS/workflow2

# 2. Create .env file (see above)

# 3. Build and run with Docker Compose
docker-compose up --build

# 4. Access at http://localhost:5000
```

**Alternative Docker commands:**
```bash
# Build the image locally
docker build -t corner-man-os .

# Run the container
docker run -p 5000:5000 --env-file .env corner-man-os
```

#### ⚠️ Docker Limitation: WhatsApp Mocking

**Important:** The Docker version **does NOT support actual WhatsApp messaging** due to headless environment limitations.

- **What happens:** WhatsApp messages are **mocked** (logged to console only)
- **Why:** Docker containers are headless (no GUI), and `pywhatkit` requires a browser
- **Console output example:**
  ```
  🐳 [DOCKER MODE] Mocking WhatsApp send to +33753862654: Reminder: The fight is tomorrow!
  ✅ Message sent successfully (Mocked).
  ```
- **Solution:** Use the local installation method below for real WhatsApp functionality

---

### Local Installation (with WhatsApp Support)

For **full WhatsApp functionality**, install locally with `pywhatkit`.

**Prerequisites:**
- Python 3.10+
- Chrome browser (required for pywhatkit)
- Git

**Steps:**

1. **Clone the repository**
```bash
git clone https://github.com/Andy12-14/Corner-Man-OS.git
cd Corner-Man-OS/workflow2
```

2. **Create virtual environment**
```bash
# Create venv
python -m venv .venv

# Activate (Git Bash / Linux / macOS)
source .venv/Scripts/activate

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```bash
# Install base requirements
pip install -r requirements.txt

# Install WhatsApp support (REQUIRED for WhatsApp functionality)
pip install pywhatkit PyAutoGUI
```

4. **Create `.env` file** (see Prerequisites section above)

5. **Run the application**
```bash
python main.py
```

6. **Access the web interface**
   - Open your browser to: http://localhost:5000

#### WhatsApp Setup (Local Only)

When running locally with `pywhatkit`:

1. **How it works:**
   - Opens WhatsApp Web in Chrome automatically
   - Sends messages via browser automation
   - You must be logged into WhatsApp Web

2. **First time setup:**
   - Make sure Chrome is installed
   - Log into WhatsApp Web (https://web.whatsapp.com)
   - Keep "Stay signed in" checked

3. **Default phone number:** `+33753862654` (can be changed in agent prompts)

---

## Usage Guide

### Web Interface

1. Navigate to http://localhost:5000
2. Click on any of the three agents:
   - **Headhunter** - Find boxer profiles
   - **Smoke Detector** - Find upcoming fights
   - **The Plug** - Get boxing news
3. Type your query in the chat interface
4. The agent will process your request and display results

### Agent-Specific Tips

#### 🎯 Headhunter Agent

**What it does:**
- Searches BoxRec for boxer profiles
- Finds YouTube highlights
- Retrieves boxer images

**Example queries:**
- "Terence Crawford"
- "Canelo Alvarez"
- "Gervonta Davis"

**⚠️ Important Notes:**

- **The agent is not perfect** - sometimes you may need to retry
- For **established stars** (e.g., Terence Crawford, Canelo Alvarez):
  - Usually works on first try
  - If it fails, **type the name 2-3 times**
- For **upcoming prospects** (e.g., Abdullah Mason):
  - May require multiple attempts
  - Less online data available
  - Be patient and retry

**Tips if the agent doesn't find the boxer:**
1. Type the full name again (2-3 times)
2. Try different name formats:
   - "Crawford" vs "Terence Crawford"
   - "Canelo" vs "Saul Alvarez"
3. Check spelling
4. Wait a moment between retries (API rate limits)

**Why it might fail:**
- BoxRec search returns no results
- Boxer has limited online presence
- Name spelling variations
- API rate limits or 503 errors

#### 🔥 Smoke Detector Agent

**What it does:**
- Finds upcoming boxing fights from box-live
- Can set WhatsApp reminders (local version only)

**Example queries:**
- "upcoming fights"
- "what fights are coming up?"
- "show me the next big fights"
- "set a reminder for the Crawford fight" (local only)

**WhatsApp Reminders:**
- **Local version:** ✅ Fully functional with pywhatkit
- **Docker version:** ❌ Mocked (logged to console only)

#### 📰 The Plug Agent

**What it does:**
- Scrapes ESPN for boxing news
- Can send news via WhatsApp (local version only)

**Example queries:**
- "latest boxing news"
- "what's happening in boxing?"
- "give me the news"
- "send me the latest updates" (local only)

### Media Display

The web interface automatically handles rich media:
- **YouTube videos:** Embedded as playable iframes
- **Images:** Displayed inline with proper styling
- **Links:** Clickable and formatted

---

## WhatsApp Integration

### Local Version (Full Support) ✅

When running locally with `pywhatkit` installed:

**Installation:**
```bash
pip install pywhatkit PyAutoGUI
```

**How it works:**
1. Opens WhatsApp Web in Chrome
2. Sends messages automatically
3. Requires you to be logged into WhatsApp Web
4. Works with both Smoke Detector and The Plug agents

**Default phone number:** `+33753862654` (configurable in agent prompts)

### Docker Version (Mocked) ⚠️

When running in Docker:

- WhatsApp messages are **NOT actually sent**
- Messages are logged to the console with `🐳 [DOCKER MODE]` prefix
- This prevents crashes in the headless Docker environment

**Example console output:**
```
🐳 [DOCKER MODE] Mocking WhatsApp send to +33753862654: Reminder: The fight is tomorrow!
✅ Message sent successfully (Mocked).
```

**Why Docker doesn't support WhatsApp:**
- Docker containers are "headless" (no GUI/screen)
- `pywhatkit` requires Chrome browser to open WhatsApp Web
- Browser automation doesn't work in headless environments

**Alternatives for Docker:**
1. Use local installation for WhatsApp functionality
2. Integrate a proper API:
   - Twilio WhatsApp API (recommended for production)
   - WhatsApp Business API
   - Other messaging services

---

## Troubleshooting

### Common Issues

**1. "No module named 'ddgs'" or import errors**

**Solution:** Rebuild Docker image
```bash
docker-compose down
docker-compose up --build
```

**2. "127.0.0.1 didn't send any data" in Docker**

**Solution:** Already fixed in current version
- Ensure `main.py` has `app.run(host='0.0.0.0', port=5000)`

**3. Agent doesn't find boxer information**

**Solutions:**
- Try typing the name 2-3 times
- Check spelling carefully
- Try full name vs. last name only
- For prospects, be patient - may require multiple attempts
- Wait between retries (API rate limits)

**4. API errors (503, rate limits)**

**Solutions:**
- The agents have built-in error handling
- Wait a moment and try again
- Check your API keys in `.env`
- Verify API keys are valid and have credits

**5. WhatsApp not working**

**Docker:** Expected behavior - use local version for WhatsApp
**Local:** 
- Ensure `pywhatkit` is installed: `pip install pywhatkit PyAutoGUI`
- Log into WhatsApp Web in Chrome
- Check Chrome is installed and accessible

**6. Docker container won't start**

**Solutions:**
```bash
# Check if port 5000 is already in use
docker ps

# Stop all containers
docker-compose down

# Rebuild and restart
docker-compose up --build
```

### Agent Limitations

- **Not 100% reliable:** AI agents may occasionally fail or return incomplete data
- **Retry mechanism:** Simply re-submit your query if it doesn't work the first time
- **Data availability:** Works best with well-known boxers who have extensive online records
- **Upcoming prospects:** May struggle with fighters who have limited BoxRec/media presence
- **API dependencies:** Relies on external APIs (Gemini, ScrapeGraph) which may have rate limits

---

## Project Structure

```
workflow2/
├── main.py                 # Flask web application
├── headhunter.py          # Headhunter agent
├── smoke_detector.py      # Smoke Detector agent
├── The_plug.py            # The Plug agent
├── call_functions.py      # Function dispatcher for agents
├── Tools/
│   └── tools.py           # Agent tools and schemas
├── templates/             # HTML templates for web UI
│   ├── base.html
│   ├── index.html
│   └── agent.html
├── static/
│   └── style.css          # Boxing-themed styling
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
└── .env                   # Environment variables (not committed)
```

---

## Development

### Running Tests
```bash
pytest
```

### Code Structure
- `main.py`: Flask routes and web server
- `{agent}.py`: Agent logic and AI prompts
- `Tools/tools.py`: Scraping functions and schemas
- `call_functions.py`: Function dispatcher

### Adding New Features
1. Add tool function to `Tools/tools.py`
2. Create schema in `Tools/tools.py`
3. Update agent system prompt
4. Add function to `call_functions.py` dispatcher

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

---

## Links

- **Docker Hub:** https://hub.docker.com/r/andy94500/corner-man-os
- **GitHub Repository:** https://github.com/Andy12-14/Corner-Man-OS
- **Google Gemini API:** https://ai.google.dev/
- **ScrapeGraph API:** https://scrapegraphai.com/

---

## License

This project is open source and available under the MIT License.

---

## Contact

- **Maintainer:** Andy
- **GitHub:** [@Andy12-14](https://github.com/Andy12-14)
- **Repository:** [Corner-Man-OS](https://github.com/Andy12-14/Corner-Man-OS)

---

## Acknowledgments

- Powered by **Google Gemini AI**
- Web scraping by **ScrapeGraph**
- Boxing data from **BoxRec**, **box-live**, and **ESPN**

---

**⚠️ Disclaimer:** This is an AI-powered project. Results may vary based on data availability and API performance. Always verify critical information from official sources. This project is for educational and personal use only.
