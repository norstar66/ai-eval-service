# TODO: v0.2 expansion (Deterministic)

## Evaluation Strategy

### TODO: Metric 2: Response Quality - v0.2 expansion

- grammar and spelling
- clarity and coherence
- relevance to the prompt

### TODO: Metric 3: Response Relevance - v0.2 expansion

- relevance to the prompt
- accuracy of information
- completeness of response

## Expancd Scope for Request and Response

### Example Request

```json
{
  "prompt": "What is the capital of France?",
  "model": "gpt-3.5-turbo",
  "max_tokens": 100,
  "temperature": 0.7,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "stop": ["\n"],
  "max_retries": 3,
  "timeout": 30,
  "sentence_count": 1,
  "word_count": 10,
  "character_count": 100
}
```

### Example Response

```json
{
  "prompt": "What is the capital of France?",
  "model": "gpt-3.5-turbo",
  "max_tokens": 100,
  "temperature": 0.7,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "stop": ["\n"],
  "max_retries": 3,
  "timeout": 30,
  "sentence_count": 1,
  "word_count": 10,
  "character_count": 100,
  "response": "The capital of France is Paris.",
  "sentence_count": 1,
  "word_count": 10,
  "character_count": 100,
  "evaluation": {
    "sentence_count": true,
    "word_count": true,
    "character_count": true
  }
}
```
