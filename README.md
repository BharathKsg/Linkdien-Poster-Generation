# 🧠 LinkedIn-Poster-Generation

An AI-powered service that generates LinkedIn posts reflecting a client physician's perspective on healthcare AI topics.

## 🚀 Features

- Generate professional, physician-style LinkedIn posts using AI
- REST API backend with FastAPI
- Interactive frontend with Streamlit

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI for backend API
- Streamlit for frontend interface
- OpenAI / NLP libraries for content generation (customize as needed)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/BharathKsg/Linkdien-Poster-Generation
cd LinkedIn-Poster-Generation
```

### 2. Create a virtual environment (recommended)
```python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```


### 4.Backend (FastAPI)
```fastapi dev main.py```
The FastAPI server will be available at:
http://127.0.0.1:8000

###5. Frontend (Streamlit)
In a separate terminal (ensure the same virtual environment is active):

```streamlit run streamlit_main.py```

