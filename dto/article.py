from dataclasses import dataclass


@dataclass(frozen=False)
class Article:
    title: str
    url: str
    polarity_score: float = None
    subjectivity_score: float = None
    created_at: str = None
