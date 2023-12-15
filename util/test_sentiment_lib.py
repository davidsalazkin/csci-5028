from util.sentiment_lib import SentimentLib
from dto.article import Article


def test_positive_sentiment_analysis():
    article = Article(title="this is a happy message!")
    article = SentimentLib.get_sentiment(article)
    assert article.polarity_score > 0.5


def test_negative_sentiment_analysis():
    article = Article(title="YUCK THIS IS AN ANGRY MESSAGE!!!")
    article = SentimentLib.get_sentiment(article)
    assert article.polarity_score < 0.5

def test_subjective_sentiment_analysis():
    article = Article(title="maybe if i had to guess i am happy or maybe angry.")
    article = SentimentLib.get_sentiment(article)
    assert article.subjectivity_score > 0.5


def test_objective_sentiment_analysis():
    article = Article(title="this is a fact.")
    article = SentimentLib.get_sentiment(article)
    assert article.subjectivity_score < 0.5
