# 노션에 쓰는 함수만 넣는다.

from config import NOTION_PRICE_DB_ID
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from data.domestic_stock import get_naver_prop, get_yfinance_prop

def update_stock_DB(page, stock_info):
    notion.pages.update(
        page_id=page[NOTION_PRICE_DB_ID],
        properties=stock_info
    )
