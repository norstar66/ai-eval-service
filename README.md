# Project Map

```bash

ai_eval_&_inf_service/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── llm_client.py
│   ├── evaluator.py
│   ├── logger.py
│   └── config.py
│
├── tests/
│   └── test_health.py
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .dockerignore

```

# Setup

## Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application Locally

```bash
uvicorn app.main:app --reload
```

### visit:

- http://localhost:8000/health, you should see {"status": "ok"},
- http://localhost:8000/docs, you should see the API docs.
- If both work, scaffolding is correct.
