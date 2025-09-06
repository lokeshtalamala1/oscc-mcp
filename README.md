# Open Source Contribution Concierge (OSCC)

## 📌 Project Overview
Open-Source Contribution Concierge (OSCC) is an **AI-powered agent** that helps new developers start contributing to open-source by:
- Finding **beginner-friendly GitHub issues**.
- Summarizing them in **simple language**.
- Creating **Notion tasks** or posting **Slack notifications**.
- Using **Descope Outbound Apps** for **secure authentication** (no hardcoded tokens).

This project was built for the **Descope MCP Hackathon 2025 (Theme 1: Agents That Act to Help).**

---

## 🚀 Features
- 🔎 Search GitHub issues tagged `good first issue`
- 🧠 AI-powered summarization of issue descriptions
- 📋 Automatic Notion task creation
- 💬 Slack notifications for team updates
- 🔐 Secure OAuth-based token handling with **Descope**

---

## 🛠️ Tech Stack
- **Backend:** Python (FastAPI)
- **Frontend:** Next.js + Tailwind
- **AI:** LangChain / LLM APIs
- **Authentication:** Descope Outbound Apps
- **Integrations:** GitHub API, Notion API, Slack API
- **Deployment:** Docker + Vercel

---

## 📂 Project Structure
```
oscc-mcp/
│── README.md
│── docker-compose.yml
│── .env.sample
│── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── github_service.py
│   │   ├── notion_service.py
│   │   ├── slack_service.py
│   │   ├── auth_service.py
│   │   └── summarizer.py
│   └── utils/logger.py
│
│── frontend/
│   ├── pages/
│   │   ├── index.js
│   │   └── dashboard.js
│   ├── components/IssueCard.js
│   ├── package.json
│   └── tailwind.config.js
│
└── tests/
    ├── test_github.py
    ├── test_notion.py
    └── test_auth.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-team/oscc-hackathon.git
cd oscc-hackathon
```

### 2️⃣ Configure Environment
Copy `.env.sample` to `.env` and fill in values:
```env
DESCOPE_PROJECT_ID=xxxx
DESCOPE_CLIENT_ID=xxxx
DESCOPE_CLIENT_SECRET=xxxx

GITHUB_ORG=openai
GITHUB_REPO=openai-api
NOTION_TOKEN=secret_xxx
SLACK_BOT_TOKEN=xoxb-xxx
OPENAI_API_KEY=sk-xxxx
```

### 3️⃣ Run with Docker
```bash
docker compose up --build
```

- Backend: http://localhost:8000  
- Frontend: http://localhost:3000  

### 4️⃣ Run without Docker
#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```
#### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Running Tests
```bash
pytest tests/
```

---

## 🎥 Demo
- **Demo & Walkthrough (YouTube):** [https://youtu.be/NKL9icBUGwM](https://youtu.be/NKL9icBUGwM)

---

## 👨‍💻 Team
- Team OSCC - Lokesh Talamala

---

## 📌 Future Improvements
- Support for Trello / Jira
- Advanced issue matching (skills → issues)
- Multi-language summarization
- GitHub PR drafting
