# 주가를 가져오는 함수만 포함시키기

import yfinance as yf      # Yahoo 증권에서 데이터 받아오기
import requests            # 네이버 증권에서 데이터 받아오기

def get_naver_prop(ticker):

    # 네이버는 브라우저가 아닌 프로그램의 요청을 차단하는 경우가 있어서, 브라우저인 척 속이는 역할 수행
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = (
        f"https://polling.finance.naver.com/api/realtime"
        f"?query=SERVICE_ITEM:{ticker}"
    )

    data = requests.get(
        url,
        headers=headers,
        timeout=10 # 최대 10초까지만 기다리겠다는 의미.
    ).json()

    item = data["result"]["areas"][0]["datas"][0]
  
    return {
        "price": item["nv"],   # 현재가
        "change": item["cv"],  # 전일 대비 가격 변화(원)
        "rf": item["rf"],      # 등락 구분(상승/하락/보합을 나타내는 코드)
        "cr": item["cr"],      # 등락률(%)
        "countOfListedStock": item["countOfListedStock"]  # 상장주식수
    }


def get_yfinance_prop(ticker):

    stock = yf.Ticker(f"{ticker}.KS")   
    info = stock.info
    market_cap = info.get("marketCap", 0)
            
    if market_cap is None:
        market_cap = 0

    high_52 = info.get("fiftyTwoWeekHigh")
    low_52 = info.get("fiftyTwoWeekLow")

    currency = info.get("currency")
    country = info.get("country")
    sector = info.get("sector")
    industry = info.get("industry")

    return {
        "high_52": high_52,
        "low_52": low_52,
        "currency": currency,
        "country": country,
        "sector": sector,
        "industry": industry
    }
