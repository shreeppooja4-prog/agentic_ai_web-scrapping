# Agentic AI Web Scraper

## Project Overview
Agentic AI Web Scraper is a Python desktop application that can:
1. Scrape textual content from any website.
2. Store meaningful paragraphs.
3. Answer user questions intelligently using OpenAI GPT models.

The tool combines web scraping, AI question answering, and a GUI interface for interactive use.

---

## Features
- Scrape website content automatically.
- Ask natural language questions about the scraped content.
- Controlled memory: limits context for faster AI responses.
- User-friendly GUI using Tkinter.
- Error handling for invalid URLs and empty inputs.

---

## Technical Stack
| Component | Technology | Role |
|-----------|------------|------|
| Web Scraping | `requests` + `BeautifulSoup` | Fetch and parse website content |
| AI Agent | `openai` GPT-4o-mini | Generates answers to user questions |
| GUI | Tkinter | User interface for input and output |
| Environment Management | `python-dotenv` | Stores API keys securely |

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/username/AgenticAI-WebScraper.git
cd AgenticAI-WebScraper

2.Create and activate a virtual environment

3.Install dependencies
pip install -r requirements.txt

4. Setup OpenAI API key
Create a .env file:
    OPENAI_API_KEY=your_openai_api_key_here
5.Run the program
    python main.py

Usage
1. Enter the website URL and click Scrape Website.
2. Wait for the message confirming the paragraphs were stored.
3. Enter your question and click Ask Agent.
4. The AI will provide a concise answer in the output box.

Future Enhancements:
Add multi-page scraping.
Summarization and keyword extraction.
Offline AI model support.
Improved GUI styling and UX.

