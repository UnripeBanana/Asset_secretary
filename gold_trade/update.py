from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

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
