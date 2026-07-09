from datetime import datetime
from zoneinfo import ZoneInfo
from domestic_stock.read import get_ticker
from domestic_stock.update import update_stock_DB
from data.domestic_stock import get_naver_prop, get_yfinance_prop
from history.history import append_prices

def domestic_stock_main(pages):
    today = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d")
    history_rows = []

    for page in pages:
        ticker = get_ticker(page)
        if not ticker:
            continue

        stock_info = {
            **get_naver_prop(ticker),
            **get_yfinance_prop(ticker)
        }

        update_stock_DB(page, stock_info)

        history_rows.append({
            "date": today,
            "ticker": ticker,
            "open": stock_info["open"],
            "high": stock_info["high"],
            "low": stock_info["low"],
            "close": stock_info["price"],
            "volume": stock_info["volume"]
        })

    append_prices(history_rows)
