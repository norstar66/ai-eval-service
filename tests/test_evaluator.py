from app.evaluator import evaluate_response

def test_perfect_pass_score_1():
    r = evaluate_response(
        response_text="This is a perfect response.",
        max_sentences=1,
        max_words=30,
        max_characters=200,
    )
    assert r.metrics.sentence_count <= 1
    assert r.evaluation["score"] == 1.0
    assert r.evaluation["passed_constraints"] is True

def test_sentence_fail_only():
    r = evaluate_response(
        "One. Two.",
        max_sentences=1,
        max_words=30,
        max_characters=200,
    )
    assert r.evaluation["sentence_pass"] is False
    assert r.evaluation["word_pass"] is True
    assert r.evaluation["character_pass"] is True
    assert r.evaluation["score"] == 0.5  # only word+char pass -> 0.2 + 0.3
    assert r.evaluation["passed_constraints"] is False

def test_word_fail_only():
    long_text = "word " * 31
    r = evaluate_response(
        long_text.strip() + " ",
        max_sentences=1,
        max_words=30,
        max_characters=1000,
    )
    assert r.evaluation["sentence_pass"] is True
    assert r.evaluation["word_pass"] is False
    assert r.evaluation["character_pass"] is True
    assert r.evaluation["score"] == 0.7  # only word+char pass -> 0.5 + 0.2
    assert r.evaluation["passed_constraints"] is False

def test_character_fail_only():
    r = evaluate_response(
        "a" * 1001,
        max_sentences=1,
        max_words=500,
        max_characters=200,
    )
    assert r.evaluation["sentence_pass"] is True
    assert r.evaluation["word_pass"] is True
    assert r.evaluation["character_pass"] is False
    assert r.evaluation["score"] == 0.8
    assert r.evaluation["passed_constraints"] is False