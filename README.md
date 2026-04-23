About
LLM Cost Planner is a Streamlit web application that helps engineering teams, product managers, and founders understand what their AI inference will actually cost — before they ship.
You enter a model, your token usage, and your expected call volume. The app returns a full cost breakdown across seven modules: per-request cost, model comparison, scale projection, caching savings, break-even analysis, gross margin, and optimization recommendations. Everything runs in one place, with no spreadsheets required.

Installation
Requirements: Python 3.10+
bash# Clone the repository
git clone https://github.com/YOUR_USERNAME/llm-cost-planner.git
cd llm-cost-planner

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
.\venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

Usage
bashstreamlit run app/main.py
Open http://localhost:8501 in your browser.

Select a model from the sidebar
Enter your input tokens, output tokens, and daily API call volume
Set optional parameters — cache hit rate, revenue per user, current users, target margin
Click Calculate Costs
Browse the seven result tabs

Deployment
Streamlit Community Cloud — free, no server required.

Push your project to a public GitHub repository
Go to share.streamlit.io and sign in with GitHub
Click New app
Set the repository, branch to main, and main file path to app/main.py
Click Deploy

Your app will be live in about a minute at:
https://YOUR_USERNAME-llm-cost-planner.streamlit.app