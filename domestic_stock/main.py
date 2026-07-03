from config import NOTION_PRICE_DB_ID
from notion.get_all_pages import get_all_pages
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할


for page in get_all_pages(DATABASE_ID):

  props = page["properties"]

  ticker_data = props["티커"]["rich_text"]

  if len(ticker_data) == 0:
      continue

  ticker = ticker_data[0]["plain_text"]
