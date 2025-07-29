

# AI Interviewer for GitHub Repositories

This project is an interactive AI-powered interviewer that analyzes any GitHub repository and asks intelligent, technical questions based on its contents. Designed to simulate real interview scenarios, it helps developers and teams evaluate codebases, understand project structure, and prepare for interviews or code reviews.

---

##  Features

-  Parses and analyzes public GitHub repositories
-  Uses LLMs (like GPT or Mistral) to generate custom interview questions
-  Interactive frontend interface with real-time feedback
-  Fast, lightweight backend (Python + FastAPI)
-  Simple UI built with HTML/CSS/JS

---

##  Tech Stack

- **Backend**: Python, FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **LLM Engine**: OpenAI / Mistral (configurable)
- **Templates**: Jinja2
- **Deployment Ready**: Easily dockerized or hosted locally

---

##  Folder Structure

ai_interviewer/
├── backend/
│ ├── github_parser.py # Extracts and processes GitHub repo content
│ ├── llm_engine.py # Interfaces with the LLM (e.g. OpenAI, qwen2.5vl:7b)
│ ├── main.py # FastAPI server and route handler
│ └── utils.py # Shared utility functions
│
├── static/
│ ├── script.js # Handles frontend interactions and API calls
│ └── style.css # Styling for the interview UI
│
├── templates/
│ └── interview.html # Main frontend HTML page served via Jinja2
│
├── venv/ # Python virtual environment (ignored by Git)
├── .gitignore # Files and folders to be ignored by Git
├── README.md # This file
└── requirements.txt # Python dependencies
