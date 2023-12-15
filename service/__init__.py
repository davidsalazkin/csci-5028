from service.article_service import ArticleService
from util.supabase_client import SupabaseClient

article_service = ArticleService(SupabaseClient())
