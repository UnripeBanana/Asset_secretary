# 금 시세만 가져온다.

import requests            # 네이버 증권에서 데이터 받아오기

url = "https://m.stock.naver.com/front-api/realTime/marketIndex/metals"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
