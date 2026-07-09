# 노션에 쓰는 함수만 넣는다.

from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.logger import logging

def update_bond_etf_DB(page, stock_info):

    change = stock_info["change"]
    upanddown = stock_info["cr"]
    # 하락이면 음수로 변경
    if stock_info["rf"] == "5":
        change = -change
        upanddown = -upanddown
    
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
        "마지막 업데이트": rich_text(logging())
    }
    
    notion.pages.update(
        page_id=page["id"],
        properties=stock_info_mod
    )
