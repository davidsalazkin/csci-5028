"""
Houses higher level orchestral functions for articles.
"""

from typing import List

import requests

from dto.article import Article
from util.supabase_client import SupabaseClient


class ArticleService:

    def __init__(self):
        self.supabase_client = SupabaseClient()

    def fetch_articles(self, search_term: str) -> List[Article]:
        """
        Fetches a list of articles from REST API sources.
        :param search_term: The search term to use in the query.
        :return: A list of Article objects.
        """
        api_endpoint = 'https://search.prod.di.api.cnn.io/content'
        params = {
            'q': search_term,
            'size': 100,
            'from': 0,
            'sort': 'newest'
        }
        r_json = requests.get(api_endpoint, params=params).json()
        response = []
        for item in r_json.get('result'):
            response.append(
                Article(
                    title=item.get('headline'),
                    url=item.get('path')
                )
            )
        return response

    def scrape_articles(self) -> None:
        """
        A function that orchestrates the scraping of articles.
        :return:
        """
        articles = self.fetch_articles('biden')
        self.supabase_client.save_articles_to_db(articles)

    def fetch_articles_from_db(self) -> List[Article]:
        supa_response = self.supabase_client.fetch_articles()

        response = []
        for item in supa_response:
            response.append(
                Article(
                    item.get('title'),
                    item.get('url'),
                    item.get('polarity_score'),
                    item.get('subjectivity_score'),
                    item.get('created_at')
                )
            )
        return response
