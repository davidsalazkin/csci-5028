from dataclasses import dataclass


@dataclass(frozen=False)
class Article:
    title: str = None
    url: str = None
    polarity_score: float = None
    subjectivity_score: float = None
    created_at: str = None
