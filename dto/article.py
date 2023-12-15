from dataclasses import dataclass


@dataclass(frozen=True)
class Article:
    title: str
    url: str
    polarity_score: float
    subjectivity_score: float
    created_at: str = None
