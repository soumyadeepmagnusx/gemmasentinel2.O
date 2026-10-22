# 🛡️ GemmaSentinel Voice & Cloud
### Autonomous Open-Weight AI Agent for Code Security, Oracle SQL Tuning & Voice Alerting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest-2026-blueviolet.svg)](https://hacktoberfest.com/)
[![MLH Member Event](https://img.shields.io/badge/MLH-HackDay%20Kolkata-red.svg)](https://mlh.io/)
[![Model: Gemma-2-9B](https://img.shields.io/badge/Model-Gemma--2--9B--It-blue.svg)](https://ai.google.dev/gemma)
[![Deployment: DigitalOcean](https://img.shields.io/badge/Deploy-DigitalOcean-0080FF.svg)](https://www.digitalocean.com/)

---

## 🌟 Short Project Description
During **Hacktoberfest**, open-source maintainers face immense burnout reviewing high volumes of PRs, triaging security vulnerabilities (SQL injections, exposed API tokens, buffer overflows), and debugging inefficient database queries.

**GemmaSentinel Voice & Cloud** is an autonomous, open-weight developer copilot and agent harness built to protect repositories. It:
1. 🔍 **Audits Source Code & PR Diffs** for security vulnerabilities and auto-generates unit tests.
2. 🗄️ **Optimizes Oracle Database Queries** and analyzes cost-based execution plans for high-throughput enterprise workloads.
3. 🔊 **Generates Real-Time Voice Briefings** via **ElevenLabs** so maintainers receive audible vulnerability alerts without tab-switching.
4. 🍃 **Logs Security Telemetry to MongoDB Atlas** for long-term health tracking.
5. 🌊 **Deploys Seamlessly to DigitalOcean** via ready App Platform configurations.

---

## 🏆 Targeted MLH & Event Prize Tracks
- 🥇 **Best Open-Source AI Project:** Built on open-weight AI (Gemma 2) with a 100% open-source MIT codebase.
- 🥇 **Best Use of Gemma:** Powered by Google's `gemma-2-9b-it` open-weights multimodal architecture.
- 🥇 **Best Use of ElevenLabs:** Natural-sounding synthetic voice generation for instant audio security alerts.
- 🥇 **Best Use of DigitalOcean:** Cloud-ready deployment spec for DigitalOcean App Platform (`.do/app.yaml`).
- 🥇 **Best Use of MongoDB Atlas:** Cloud persistence layer tracking scan telemetry, vulnerabilities, and repo history.
- 🤝 **Title Partner Synergy:** Specialized Oracle SQL & Cost-Based Optimizer module for **Oracle Kolkata Community**.

---

## 🛠️ Technology Stack
- **Frontend / Dashboard:** Streamlit (Python, custom dark modern developer theme)
- **Core Reasoning AI:** Google **Gemma 2 (9B Instruction-Tuned)** open-weight model
- **Inference Acceleration:** Groq LPU Cloud (sub-second token generation)
- **Voice Synthesis:** ElevenLabs Neural Audio API (`eleven_multilingual_v2`)
- **Database & Telemetry:** MongoDB Atlas (M0 Cloud Cluster)
- **Infrastructure & Hosting:** DigitalOcean App Platform / Docker

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
- `python-dotenv` (BSD-3-Clause)

---

## ⏱️ What Was Built During the Hack Day
- **Pre-Build Foundation (Allowed 30%):** UI layout skeleton, environment templates, `.do/app.yaml` deployment manifest, and MIT license setup.
- **Hacking Period Execution (70%):**
  - Chained Gemma-2 prompt logic for CWE vulnerability classification.
  - Built the specialized Oracle SQL Cost-Based Optimizer engine.
  - Integrated ElevenLabs audio streaming for real-time voice alert synthesis.
  - Implemented MongoDB Atlas telemetry schema for historical vulnerability metrics.
  - Tested edge-case code samples (SQLi, ReDoS, Deserialization RCE).

---

## 🧠 What Was Learned
- **Open-Weight AI Harnesses:** Orchestrating Google's open-weight Gemma-2 for deterministic code analysis rather than generic conversational chat.
- **Sensory Multimodal UX:** Understanding how pairing visual diffs with synthetic audio alerts drastically reduces developer alert fatigue.
- **Enterprise Database Optimization:** Crafting automated rules for Oracle SQL query restructuring and Sargable index usage.

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
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE) — free and open for the community.
