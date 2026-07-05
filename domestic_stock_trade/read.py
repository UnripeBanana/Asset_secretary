from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할

def read_trade_db(NOTION_TRADE_DB_ID):

    response = notion.databases.query(
        database_id=NOTION_TRADE_DB_ID
    )

    trades = []

    for page in response["results"]:

        props = page["properties"]

        trade = {

            "page_id": page["id"],

            # 관계형
            "ticker": (
                props["종목명"]["select"]["name"]
                if props["종목명"]["select"] else None
            ),

            # 선택
            "type": props["매수/매도"]["select"]["name"],

            # 날짜
            "date": props["날짜"]["date"]["start"],

            # 숫자
            "qty": props["수량"]["number"],

            "price": props["단가"]["number"],

            "amount": props["거래금액"]["formula"]["number"]

        }

        trades.append(trade)

    return trades
