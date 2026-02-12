from pydantic import BaseModel


class InferenceRequest(BaseModel):
    prompt: str
    model: str
    max_sentences: int
    max_words: int
    max_characters: int