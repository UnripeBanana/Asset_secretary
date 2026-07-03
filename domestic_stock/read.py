from config import NOTION_PRICE_DB_ID
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.get_all_pages import get_all_pages()

def get_ticker(page):
    ticker_data = page["properties"]["티커"]["rich_text"]

    if not ticker_data:
        return None

    return ticker_data[0]["plain_text"]
