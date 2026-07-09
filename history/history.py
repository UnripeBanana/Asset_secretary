import os
import pandas as pd

CSV_PATH = "history/price_history.csv"

def append_price(ticker, date, price):

    # CSV 읽기
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
    else:
        df = pd.DataFrame(columns=[
            "date",
            "ticker",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ])

    # 오늘 데이터
    row = {
        "date": date,
        "ticker": ticker,
        "open": price["open"],
        "high": price["high"],
        "low": price["low"],
        "close": price["price"],
        "volume": price["volume"]
    }

    # 이미 존재하면 덮어쓰기
    mask = (
        (df["date"] == date) &
        (df["ticker"] == ticker)
    )

    if mask.any():
        df.loc[mask] = row
    else:
        df = pd.concat(
            [df, pd.DataFrame([row])],
            ignore_index=True
        )

    df.to_csv(CSV_PATH, index=False)
