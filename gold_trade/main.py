from domestic_stock_trade.read import read_trade_db
from domestic_stock_trade.update import update_trade_page
from trade.fifo import group_by_ticker, process_fifo

def domestic_stock_trade_main(NOTION_TRADE_DB_ID):
    trades = read_trade_db(NOTION_TRADE_DB_ID)
    trades.sort(key=lambda x: x["date"])
    
    groups = group_by_ticker(trades)
    results = process_fifo(groups)
    
    for ticker, result in results.items():
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
    
