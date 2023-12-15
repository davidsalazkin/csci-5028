import os
from typing import List
from dataclasses import asdict

from supabase import create_client

from dto.article import Article


class SupabaseClient:

    def __init__(self):
        url = os.environ.get('SUPABASE_URL')
        key = os.environ.get('SUPABASE_KEY')
        self.client = create_client(url, key)

    def save_articles_to_db(self, articles: List[Article]) -> None:
        """
        Saves a single article to the database.
        :param articles: the article objects to save to the database.
        """
        self.client.table('articles').upsert([asdict(x) for x in articles]).execute()

    def fetch_articles(self):
        """
        Fetches articles from the database.
        :return: A list of articles.
        """
        response = self.client.table('articles').select('*').execute()
        return response.data
