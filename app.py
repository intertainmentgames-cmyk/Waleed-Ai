from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from langchain_community.llms import Ollama

app = FastAPI()

# Frontend connectivity configuration (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize local Llama 3 model via Ollama
try:
    model = Ollama(model="llama3")
except Exception as e:
    print("Ollama engine target status missing. Make sure ollama is active.")

class ChatRequest(BaseModel):
    user_query: str

def google_search_and_scrape(query):
    """Google par query search karke background me top websites ka text snippet scrape karna"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    search_url = f"https://www.google.com/search?q={query}"
    
    try:
        response = requests.get(search_url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        snippets = []
        for g in soup.find_all('div'):
            text = g.get_text().strip()
            if len(text) > 60 and not text.startswith("http"):
                snippets.append(text[:250])
                if len(snippets) >= 3:
                    break
        return "\n".join(snippets)
    except Exception:
        return ""

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_input = request.user_query
    
    # 1. Live Web Search Context Scrape karna
    live_context = google_search_and_scrape(user_input)
    
    # 2. Advanced Hybrid RAG Prompt Setup
    prompt = f"""
    You are an advanced, intelligent custom AI assistant. Use the following real-time web search context to give a precise and structured answer to the user.
    
    Live Internet Search Context:
    {live_context}
    
    User Query: {user_input}
    
    Instructions: If the web context contains relevant facts, prioritize them. If the web context is empty or irrelevant, use your own internal AI knowledge base to respond perfectly. Keep the tone helpful.
    """
    
    try:
        ai_response = model.invoke(prompt)
        return {"response": ai_response}
    except Exception as e:
        return {"response": f"Ollama execution exception: {str(e)}. Please check if Llama3 is running locally."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
