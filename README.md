# Custom Live-Search AI Chatbot Platform

A premium, open-source, full-stack AI Chatbot interface inspired by ChatGPT, featuring real-time web scraping and **RAG (Retrieval-Augmented Generation)** integration via local LLMs.

## 🚀 Features
- **Premium UI/UX:** Clean, dark-themed responsive chat interface.
- **Live Internet Access:** Automatically searches Google and extracts text snippets to provide up-to-date real-time answers.
- **100% Data Privacy:** Powered by local AI execution using **Ollama & Llama 3**, meaning no data leaves your local ecosystem.
- **Zero API Cost:** Completely free to run without requiring OpenAI or external commercial API tokens.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Modern Flexbox Architecture), JavaScript (Async Fetch API)
- **Backend Framework:** Python FastAPI
- **AI Core:** Ollama (Llama 3 Model)
- **Scraping Engine:** BeautifulSoup4 & Requests

## 📦 Local Installation & Setup

### Prerequisites
1. Install [Python 3.9+](https://www.python.org/downloads/)
2. Download and install [Ollama](https://ollama.com/)

### Step 1: Initialize local AI Model
Open your terminal and pull the Llama 3 model:
```bash
ollama run llama3
