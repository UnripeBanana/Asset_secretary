# 노션에 쓰는 함수만 넣는다.

from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from data.domestic_stock import get_naver_prop, get_yfinance_prop
from utils.logger import logging

def update_stock_DB(page, stock_info):

    change = price_info["change"]
    upanddown = price_info["cr"]
    # 하락이면 음수로 변경
    if price_info["rf"] == "5":
        change = -change
        upanddown = -upanddown

    countOfListedStock = price_info["countOfListedStock"]
    
    stock_info_mod = {
        "현재가_깃허브_원본": {
            "number": stock_info["price"]
        },
        "전일대비_깃허브": {
            "number": change
        },
        "등락률_깃허브_원본": {
            "number": upanddown
        },
        "시가총액_깃허브": {
            "number": stock_info["price"]*stock_info["countOfListedStock"]
        },
        "52주 최고가": {
            "number": stock_info["high_52"]
        },
        "52주 최저가": {
            "number": stock_info["low_52"]
        },
        "통화": rich_text(stock_info["currency"]),
        "국가": rich_text(stock_info["country"]),
        "업종": rich_text(stock_info["sector"]),
        "산업": rich_text(stock_info["industry"]),
        "마지막 업데이트": rich_text(logging())
    }
    
    notion.pages.update(
        page_id=page["id"],
        properties=stock_info_mod
    )
