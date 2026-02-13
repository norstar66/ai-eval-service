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
│   └── test_evaluator.py
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .dockerignore

```

# Setup

## Verify & Initialize app directory

```bash
cd ~/*/ai_eval_service
ls -lah
touch app/__init__.py
```

## Create Virtual Environment

#### If you don't have python3.12.12 installed, please install it first.

```bash
python3.12.12 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

**Note: Make sure you are in the virtual environment**

```bash
python3.12.12 -m pip install -r requirements.txt
```

### Lock dependencies (optional)

```bash
python3.12.12 -m pip freeze > requirements.lock.txt
```

## Run the Application Locally

```bash
python3.12.12 -m uvicorn app.main:app --reload
```

### Test the Application Locally:

- http://localhost:8000, you should see {"service": "ai-eval-service", "status": "ok"},
- http://localhost:8000/health, you should see {"status": "ok"},
- http://localhost:8000/docs, you should see the API docs.
- If all work, scaffolding is correct.

# Docker

## Build the Docker Image

```bash
docker build -t ai-eval-service .
```

## Run the Docker Container

```bash
docker run -p 8000:8000 ai-eval-service
```

## Test the Docker Container

- http://localhost:8000, you should see {"service": "ai-eval-service", "status": "ok"},
- http://localhost:8000/health, you should see {"status": "ok"},
- http://localhost:8000/docs, you should see the API docs.
- If all work, scaffolding is correct.

# Unit Testing

```bash
python3.12.12 -m pytest -q
```
