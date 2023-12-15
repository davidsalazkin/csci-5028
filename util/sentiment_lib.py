from textblob import TextBlob

from dto.article import Article


class SentimentLib:

    @staticmethod
    def get_sentiment(article: Article) -> Article:
        sentiment = TextBlob(article.title).sentiment
        article.polarity_score = sentiment.polarity
        article.subjectivity_score = sentiment.subjectivity
        return article
