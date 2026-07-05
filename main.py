from config import NOTION_PRICE_DB_ID, NOTION_TRADE_DB_ID
from notion.get_all_pages import get_all_pages

from domestic_stock.main import domestic_stock_main
from domestic_stock_trade.main import domestic_stock_trade_main


#domestic_stock_main(get_all_pages(NOTION_PRICE_DB_ID))
domestic_stock_trade_main(NOTION_TRADE_DB_ID)

"""
# 프로젝트의 시작점.

# 아무 계산도 하지 않는다.

# 그냥 필요한 함수들을 순서대로 실행하는 파일이다.

from config import NOTION_TOKEN, NOTION_PRICE_DB_ID, NOTION_TRADE_DB_ID
from trade_reader import read_trade_db
from fifo import group_by_ticker, process_fifo
from notion_updater import update_trade_page
from stock_updater import update_stock_prices




# 1. 노션 데이터 읽기



# 2. 주가 업데이트



# 3. 자산배분 계산



# 4. 리밸런싱 계산



# 5. 추천 생성



# 6. 노션 업데이트





# --------------------------
# 거래내역 FIFO 계산
# --------------------------

trades = read_trade_db()
trades.sort(key=lambda x: x["date"])

groups = group_by_ticker(trades)
results = process_fifo(groups)

for ticker, result in results.items():

    print(f"\n===== {ticker} =====")

    # 잔량 업데이트
    for page_id, qty in result["remaining"].items():
        update_trade_page(
            page_id=page_id,
            remaining=qty
        )

    # 실현수익 업데이트
    for page_id, profit in result["profit_by_sell"].items():
        update_trade_page(
            page_id=page_id,
            profit=profit
        )

    print(f"{ticker} 거래내역 업데이트 완료")

# --------------------------
# 현재가 업데이트
# --------------------------

print("\n현재가 업데이트 시작...\n")

update_stock_prices()

print("\n모든 업데이트 완료!")
"""
