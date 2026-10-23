# 🛡️ GemmaSentinel Voice & Cloud
### Autonomous Open-Weight AI Agent for Code Security, Oracle SQL Tuning & Voice Alerting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest-2026-blueviolet.svg)](https://hacktoberfest.com/)
[![MLH Member Event](https://img.shields.io/badge/MLH-HackDay%20Kolkata-red.svg)](https://mlh.io/)
[![Model: Gemma-2-9B](https://img.shields.io/badge/Model-Gemma--2--9B--It-blue.svg)](https://ai.google.dev/gemma)
[![Deployment: DigitalOcean](https://img.shields.io/badge/Deploy-DigitalOcean-0080FF.svg)](https://www.digitalocean.com/)
[![Voice: ElevenLabs](https://img.shields.io/badge/Voice-ElevenLabs%20Audio-orange.svg)](https://elevenlabs.io/)
[![Database: MongoDB Atlas](https://img.shields.io/badge/DB-MongoDB%20Atlas-brightgreen.svg)](https://www.mongodb.com/cloud/atlas)
[![Demo Video: Watch](https://img.shields.io/badge/Demo%20Video-Watch%20Walkthrough-red.svg?logo=youtube)](demo.mp4)

---

## 📺 Live Video Walkthrough
▶️ **[Click here to watch the full HD narrated walkthrough video (demo.mp4)](demo.mp4)** with real-time AST audit, ElevenLabs voice alerts, Oracle SQL optimization, and MongoDB Atlas telemetry.

---

## 🌟 Short Project Description
During **Hacktoberfest**, open-source maintainers face immense burnout reviewing high volumes of PRs, triaging security vulnerabilities (SQL injections, exposed API tokens, buffer overflows), and debugging inefficient database queries.

**GemmaSentinel Voice & Cloud** is an autonomous, open-weight developer copilot and agent harness built to eliminate maintainer fatigue. It:
1. 🔍 **Audits Source Code & Live GitHub Repositories** for security vulnerabilities and auto-generates unit tests.
2. 🗄️ **Optimizes Oracle Database Queries** with visual Cost-Based Optimizer (CBO) execution plan comparison and downloadable `.sql` patches.
3. 🔊 **Generates Real-Time Synthetic Voice Briefings** via **ElevenLabs** so maintainers receive audible vulnerability alerts without tab-switching.
4. 🧪 **Executes Sandboxed Automated Test Suites** using PyTest to mathematically verify code patches.
5. 📝 **Exports GitHub PR Review Comments** with collapsible diff blocks ready for maintainer triage.
6. 🍃 **Logs Security Telemetry to MongoDB Atlas** for long-term health tracking.
7. 🌊 **Containerized for DigitalOcean** via `.do/app.yaml` and a production `Dockerfile`.

---

## 🏗️ System Architecture

```text
                      ┌────────────────────────────────────────┐
                      │      GemmaSentinel Web Dashboard       │
                      │         (Streamlit + Python)           │
                      └──────────────────┬─────────────────────┘
                                         │
     ┌───────────────────┬───────────────┼───────────────┬───────────────────┐
     ▼                   ▼               ▼               ▼                   ▼
┌───────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐
│ Google Gemma2 │ │ ElevenLabs  │ │ Oracle CBO  │ │   MongoDB   │ │  DigitalOcean   │
│ (Open-Weight) │ │ Neural Audio│ │ SQL Tuner   │ │    Atlas    │ │  App Platform   │
└───────┬───────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └────────┬────────┘
        │                │               │               │                 │
  AST Security     Real-Time Voice  Execution Plan  Cloud Audit    Containerized
   Audit & Fixes     Alert Audio    Cost Reductions  Telemetry      Deployment
```

---

## 🏆 Targeted MLH & Event Prize Tracks
- 🥇 **Best Open-Source AI Project:** Built on open-weight AI (Gemma 2) with a 100% open-source MIT codebase.
- 🥇 **Best Use of Gemma:** Powered by Google's `gemma-2-9b-it` open-weights multimodal architecture.
- 🥇 **Best Use of ElevenLabs:** Natural-sounding synthetic voice generation for instant audio security alerts.
- 🥇 **Best Use of DigitalOcean:** Cloud-ready deployment spec (`.do/app.yaml`) and containerized `Dockerfile` with health checks.
- 🥇 **Best Use of MongoDB Atlas:** Cloud persistence layer tracking scan telemetry, vulnerabilities, and repo history.
- 🤝 **Title Partner Synergy:** Specialized Oracle SQL & Cost-Based Optimizer module for **Oracle Kolkata Community**.

---

## 🛠️ Technology Stack
- **Frontend / Dashboard:** Streamlit (Python, custom dark modern developer theme)
- **Core Reasoning AI:** Google **Gemma 2 (9B Instruction-Tuned)** open-weight model
- **Inference Acceleration:** Groq LPU Cloud (sub-second token generation)
- **Voice Synthesis:** ElevenLabs Neural Audio API (`eleven_multilingual_v2`)
- **Database & Telemetry:** MongoDB Atlas (M0 Cloud Cluster)
- **Containerization & Hosting:** DigitalOcean App Platform & Docker

---

## 🤖 AI Tools Used & Attribution
As required by the MLH Hack Day guidelines, AI tools used during research and development are transparently credited:
- **Google Antigravity / Gemini:** Architecture design, boilerplate assistance, and prompt engineering refinement.
- **Google Gemma 2 (`gemma-2-9b-it`):** The core open-weight engine running inside the application for AST security analysis and SQL execution plan tuning.

---

## 📚 Open-Source Libraries & Models Used
- `gemma-2-9b-it` (Google Gemma Open License)
- `streamlit` (Apache 2.0)
- `groq` (Apache 2.0)
- `elevenlabs` (MIT)
- `pymongo` (Apache 2.0)
- `requests` (Apache 2.0)
- `python-dotenv` (BSD-3-Clause)

---

## ⏱️ What Was Built During the Hack Day (Oct 23, 2026)
- **Pre-Build Foundation (Allowed 30% — Oct 22):** UI layout skeleton, environment templates, `.do/app.yaml` deployment manifest, and MIT license setup.
- **Live Hack Day Execution (70% — Oct 23):**
  - **Commit 5 (11:07 AM):** Added Live Public GitHub Repository Importer and Sandboxed PyTest test runner.
  - **Commit 6 (11:20 AM):** Built Oracle SQL Cost-Based Optimizer with Before/After visual metrics and Markdown PR Review exporter.
  - **Commit 7 (11:27 AM):** Built containerized `Dockerfile` with healthcheck for DigitalOcean App Platform and interactive CWE telemetry charts.
  - **Commit 8 (11:30 AM):** Full system architecture documentation and multi-track submission readiness.

---

## 🧠 What Was Learned
- **Open-Weight AI Harnesses:** Orchestrating Google's open-weight Gemma-2 for deterministic code analysis rather than generic conversational chat.
- **Sensory Multimodal UX:** Understanding how pairing visual diffs with synthetic audio alerts drastically reduces developer alert fatigue.
- **Enterprise Database Optimization:** Crafting automated rules for Oracle SQL query restructuring and Sargable index usage.
- **Containerized Cloud Microservices:** Packaging Streamlit applications with Docker health checks for DigitalOcean App Platform.

---

## 🚀 Quickstart (Run Locally in 2 Minutes)

### 1. Clone the repository
```bash
git clone https://github.com/soumyadeepmagnusx/gemmasentinel2.O.git
cd gemmasentinel2.O
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
Copy `.env.example` to `.env` and add your keys:
```bash
cp .env.example .env
```

### 4. Launch the dashboard
```bash
python -m streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE) — free and open for the community.
