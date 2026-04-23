
## LLM Cost Planner

## About
=======
#  LLM Cost Planner


> A Streamlit app for forecasting, comparing, and optimizing AI inference costs across major LLM providers.

---

## About

LLM Cost Planner helps engineering teams, product managers, and founders understand what their AI inference will actually cost — before they ship.

Enter a model, your token usage, and expected call volume. The app returns a full cost breakdown across seven modules:

- Per-request cost
- Model comparison
- Scale projection
- Caching savings
- Break-even analysis
- Gross margin
- Optimization recommendations

Everything runs in one place — no spreadsheets required.

---

## Installation

 Requirements
- Python 3.10+

 Clone the repository


git clone https://github.com/YOUR_USERNAME/llm-cost-planner.git
cd llm-cost-planner
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
```

```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

##  Usage

```bash
streamlit run app/main.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

##  Models Supported

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

> Pricing is managed in `config/model_pricing.json`. To update a price, edit one value in that file — no code changes needed.

---

## Deployment

Deploy using **Streamlit Community Cloud** — free, no server required.

**1.** Push your project to a public GitHub repository

**2.** Go to [https://share.streamlit.io](https://share.streamlit.io)

**3.** Sign in with GitHub

**4.** Click **New App** and fill in the following:

| Field       | Value          |
|-------------|----------------|
| Repository  | your repo      |
| Branch      | `main`         |
| Main file   | `app/main.py`  |

**5.** Click **Deploy**

Your app will be live at:

https://YOUR_USERNAME-llm-cost-planner.streamlit.app
