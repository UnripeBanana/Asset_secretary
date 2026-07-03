# 환경변수 모으기

import os

# 노션에 연결중인 현재가 DB의 토큰값.
NOTION_TOKEN = os.environ["NOTION_TOKEN"]

# 국장종목 DB 링크
NOTION_PRICE_DB_ID = os.environ["NOTION_PRICE_DB_ID"]

# 국장종목 거래내역 DB 링크
NOTION_TRADE_DB_ID = os.environ["NOTION_TRADE_DB_ID"]

