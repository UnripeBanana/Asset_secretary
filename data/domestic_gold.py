# 금 시세만 가져온다.

import requests            # 네이버 증권에서 데이터 받아오기

def get_gold_price():

    url = "https://m.stock.naver.com/front-api/realTime/marketIndex/metals"
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://m.stock.naver.com",
        "Referer": "https://m.stock.naver.com/marketindex/metals/M04020000",
    }
    
    payload = {
        "reutersCodes": ["M04020000"]
    }
    
    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=10
    )
    
    gold = response.json()["result"]["metals"]["M04020000"]

    return {
        "price": int(gold["closePrice"].replace(",", "")),           # 현재가
        "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
        "rate": float(gold["fluctuationsRatio"]),                    # 등락률
        "direction": gold["fluctuationsType"]["name"]                # 등락여부
    }

# 받을 수 있는 정보 모음
"""
price = gold["closePrice"]                  # 현재가
change = gold["fluctuations"]               # 전일대비
rate = gold["fluctuationsRatio"]            # 등락률
open_price = gold["openPrice"]              # 시가
high = gold["highPrice"]                    # 고가
low = gold["lowPrice"]                      # 저가
volume = gold["accumulatedTradingVolume"]   # 거래량
value = gold["accumulatedTradingValue"]     # 거래대금
status = gold["marketStatus"]               # OPEN / CLOSE
updated = gold["localTradedAt"]             # 갱신시각
"""
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
