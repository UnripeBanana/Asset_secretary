# 노션에 쓰는 함수만 넣는다.

from config import NOTION_DB
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from data.stock import give_properties
import os

NOTION_TOKEN = os.environ["NOTION_TOKEN"]

notion = Client(auth=NOTION_TOKEN)

def rich_text(value):
    return {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": str(value) if value else ""
                }
            }
        ]
    }

def update_trade_page(page_id, remaining=None, profit=None):

    properties = {}

    if remaining is not None:
        properties["잔량"] = {
            "number": remaining
        }

    if profit is not None:
        properties["실현수익"] = {
            "number": profit
        }

    notion.pages.update(
        page_id=page_id,
        properties=properties
    )


def update_price:
    properties = give_properties()
    notion.pages.update(
        page_id=page["id"],
        properties=properties
    )
