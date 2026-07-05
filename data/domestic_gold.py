# 금 시세만 가져온다.

import requests            # 네이버 증권에서 데이터 받아오기

def get_gold_price():

    url = "https://m.stock.naver.com/front-api/realTime/marketIndex/metals"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

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
