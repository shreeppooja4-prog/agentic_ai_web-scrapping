

import webbrowser
import threading
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

# ===================== LOAD ENV =====================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ===================== APP =====================
app = Flask(__name__)

# ===================== GLOBAL MEMORY =====================
PARAGRAPHS = []

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ===================== SCRAPER TOOL =====================
def scrape_website_logic(url):
    global PARAGRAPHS
    PARAGRAPHS = []

    res = requests.get(url, headers=HEADERS, timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")

    for p in soup.find_all("p"):
        text = " ".join(p.get_text().split())
        if len(text) > 100:
            PARAGRAPHS.append(text)

    return len(PARAGRAPHS)

# ===================== AGENT BRAIN =====================
def agent_think(question, context):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an intelligent web-scraping AI agent."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# ===================== ROUTES =====================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "URL required"})

    try:
        count = scrape_website_logic(url)
        return jsonify({"message": f"Stored {count} knowledge chunks"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/ask", methods=["POST"])
def ask():
    if not PARAGRAPHS:
        return jsonify({"error": "Scrape a website first"})

    question = request.json.get("question")
    context = "\n".join(PARAGRAPHS[:12])

    answer = agent_think(question, context)
    return jsonify({"answer": answer})

# ===================== RUN =====================

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)


