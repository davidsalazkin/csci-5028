from textblob import TextBlob

from util.sentiment_lib import SentimentLib


def test_positive_sentiment_analysis():
    example_text = "this is a happy message!"
    sentiment = TextBlob(example_text).sentiment
    assert sentiment.polarity > 0.5


def test_negative_sentiment_analysis():
    example_text = "YUCK THIS IS AN ANGRY MESSAGE!!!"
    sentiment = TextBlob(example_text).sentiment
    assert sentiment.polarity < 0.5


def test_subjective_sentiment_analysis():
    example_text = "maybe if i had to guess i am happy or maybe angry."
    sentiment = TextBlob(example_text).sentiment
    assert sentiment.subjectivity > 0.5


def test_objective_sentiment_analysis():
    example_text = "this is a fact."
    sentiment = TextBlob(example_text).sentiment
    assert sentiment.subjectivity < 0.5
