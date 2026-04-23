#LLM Cost Planner

#About

LLM Cost Planner is a Streamlit web application that helps engineering teams, product managers, and founders understand what their AI inference will actually cost — before they ship.

You enter a model, your token usage, and your expected call volume. The app returns a full cost breakdown across seven modules:

- Per-request cost  
- Model comparison  
- Scale projection  
- Caching savings  
- Break-even analysis  
- Gross margin  
- Optimization recommendations  

Everything runs in one place — no spreadsheets required.

---

#Installation

 Requirements
- Python 3.10+

 Clone the repository


git clone https://github.com/YOUR_USERNAME/llm-cost-planner.git
cd llm-cost-planner

Create and activate virtual environment
python -m venv venv
Activate
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Usage
streamlit run app/main.py

Open in browser:

http://localhost:8501

Deployment

Deploy using Streamlit Community Cloud (free, no server required)

Steps
Push your project to a public GitHub repository
Go to https://share.streamlit.io
Sign in with GitHub
Click New App
Set:
Repository → your repo
Branch → main
File → app/main.py
Click Deploy

Live URL

Your app will be live at:

https://YOUR_USERNAME-llm-cost-planner.streamlit.app
