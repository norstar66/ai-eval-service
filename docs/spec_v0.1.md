### Backend Artifact by: Andrew "Norstar" Charlton

#### Start Date: 2026-02-11

#### Target End Date: 2026-05-11

---

# Minimal AI Evaluation and Inference Service

## Overview

This service provides minimal AI evaluation and inference capabilities.

## Features

- Minimal AI evaluation and inference
- Accepts prompt via HTTP request
- Sends request to Local Ollama Model or OpenAI API
- Evaluates response with a deterministic rule/metric
- Returns structured JSON response

---

## 1. Problem Statement

- This service provides a backend system for evaluating whether an LLM-generated summary satisfies explicit structural constraints (sentence count and word count). It is designed for developers building AI-powered systems who require deterministic validation of model outputs.

### Example Request

```json
{
  "prompt": "...",
  "model": "string",
  "max_sentences": 1,
  "max_words": 30,
  "max_characters": 200
}
```

### Example Response

```json
{
  "prompt": "What is the capital of France?",
  "metrics": {
    "sentence_count": 1,
    "word_count": 10,
    "character_count": 100,
    "latency_ms": 812
  },
  "evaluation": {
    "sentence_pass": true,
    "word_pass": true,
    "character_pass": true,
    "score": 1.0,
    "passed_constraints": true
  }
}
```

---

## 2. Core Use Cases

- User submits a prompt to the service.
- Service sends the prompt to the Local Ollama Model or OpenAI API.
- Service evaluates the response with a deterministic rule/metric.
- Service returns the structured JSON response.

---

## 3. Functional Requirements

- REST endpoint /inference
- LLM integration (local or API)
- Logging of prompt + response
- Evaluation logic (define metric)
- /health endpoint
- Dockerized deployment
- Nothing else.

---

## 4. Non-Goals

- No UI
- No auth system
- No multi-agent orchestration
- No streaming
- No model training
- No distributed system
- Contain ambition here.

---

## 5. Architecture

- API Layer (FastAPI) — handles routing, validation, JSON serialization
- LLM Client — abstracts Ollama or OpenAI-compatible API calls
- Evaluation Module — computes deterministic metrics
- Logging Layer — writes structured JSON logs to file
- Docker Runtime — containerized deployment environment

---

## 6. Data Flow

Step-by-step:

1. Receive POST
2. Validate input
3. Call LLM
4. Run evaluation
5. Log result
6. Return JSON

Clear. Linear.

---

## 7. Evaluation Strategy (Deterministic)

### Metric 1: Response Length

- sentence count
- word count
- character count

#### Scoring

- Score range: 0.0 – 1.0
- Pass threshold: score == 1.0
- No partial classification tiers in v0.1

##### Deterministic scoring formula

- `score = ( sentence_pass * 0.5 ) + ( word_pass * 0.3 ) + ( character_pass * 0.2 )`

##### Where:

- sentence_pass = 1 if sentence_count <= max_sentences else 0
- word_pass = 1 if word_count <= max_words else 0
- character_pass = 1 if character_count <= max_characters else 0
- Score range: 0.0 – 1.0
- Pass threshold: score == 1.0
- No partial pass classification in v0.1.

---

## 8. Success Criteria

Define measurable completion:

1. p95 latency under 1500ms on local Ollama model
2. Docker build < 60 seconds
3. Logs written to /var/log/inference.log
4. Health endpoint returns 200
5. README explains setup

Concrete. Observable.
