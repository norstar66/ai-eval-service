# app/evaluator.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class EvalMetrics:
    sentence_count: int
    word_count: int
    character_count: int
    

@dataclass(frozen=True)
class EvalResult:
    metrics: EvalMetrics
    evaluation: Dict[str, object] # keeps it simple for JSON serialization
    

def _count_sentences(text: str) -> int:
    """
    Deterministic, minimal sentence counter:
    - counts segments ending in . ! ? (1+ occurrences)
    - ignores empty/whitespace
    """
    t = (text or "").strip()
    if not t:
        return 0
    
    enders = {".", "!", "?"}
    count = 0
    in_sentence = False
    
    for char in t:
        if char.strip():
            in_sentence = True
        if char in enders and in_sentence:
            count += 1
            in_sentence = False

    # If it doesn't end with punctuation but has content, count as 1 sentence.
    if count == 0 and t:
        return 1

    # If there was trailing content after last ender, count it as a sentence.
    if in_sentence:
        count += 1

    return count


def _count_words(text: str) -> int:
    """Count words in text."""
    t = (text or "").strip()
    if not t:
        return 0
    return len(t.split())


def _count_characters(text: str) -> int:
    """Count characters in text."""
    return len(text or "")


def evaluate_response (
    response_text: str,
    *,
    max_sentences: int,
    max_words: int,
    max_characters: int
) -> EvalResult:
    """
    Deterministic constraint evaluation + score:
      score = (sentence_pass*0.5) + (word_pass*0.3) + (character_pass*0.2)
      pass threshold in v0.1: score == 1.0
    """

    metrics=EvalMetrics(
        sentence_count=_count_sentences(response_text),
        word_count=_count_words(response_text),
        character_count=_count_characters(response_text),
    )
 

    sentence_pass = metrics.sentence_count <= max_sentences
    word_pass = metrics.word_count <= max_words
    character_pass = metrics.character_count <= max_characters
    
    score = (
        (1.0 if sentence_pass else 0.0) * 0.5 + \
        (1.0 if word_pass else 0.0) * 0.3 + \
        (1.0 if character_pass else 0.0) * 0.2
    )
    
    evaluation = {
        "sentence_pass": sentence_pass,
        "word_pass": word_pass,
        "character_pass": character_pass,
        "score": float(score),
        "passed_constraints": float(score) == 1.0,
    }

    return EvalResult(metrics=metrics, evaluation=evaluation)