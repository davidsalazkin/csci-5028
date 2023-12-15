from unittest.mock import MagicMock
from dto.article import Article
from service import ArticleService
from dataclasses import asdict


def test_fetch_articles():
    mock_supabase_client = MagicMock()
    mock_supabase_client.fetch_articles.return_value = [asdict(Article('test', 'test'))]
    article_service = ArticleService(mock_supabase_client)
    response = article_service.fetch_articles_from_db()
    assert len(response) == 1
