from config import NOTION_PRICE_DB_ID
from notion.get_all_pages import get_all_pages

from domestic_stock.read import get_ticker
from domestic_stock.update import update_stock_DB
from data.domestic_stock import get_naver_prop, get_yfinance_prop

for page in get_all_pages(NOTION_PRICE_DB_ID):

  ticker = get_ticker(page)
  
  stock_info = {
      **get_naver_prop(ticker),
      **get_yfinance_prop(ticker)
  }

  
