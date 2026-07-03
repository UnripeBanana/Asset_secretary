# 주가를 가져오는 함수만 포함시키기

from config import NOTION_TOKEN, NOTION_PRICE_DB_ID, NOTION_TRADE_DB_ID
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
import yfinance as yf      # Yahoo 증권에서 데이터 받아오기
import requests            # 네이버 증권에서 데이터 받아오기

def get_naver_price(code):

    # 네이버는 브라우저가 아닌 프로그램의 요청을 차단하는 경우가 있어서, 브라우저인 척 속이는 역할 수행
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = (
        f"https://polling.finance.naver.com/api/realtime"
        f"?query=SERVICE_ITEM:{code}"
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


def update_stock_prices():

    # 데이터베이스 조회
    for page in get_all_pages(DATABASE_ID):

        props = page["properties"]

        ticker_data = props["티커"]["rich_text"]

        if len(ticker_data) == 0:
            print("티커가 비어있어 건너뜀")
            continue

        ticker = ticker_data[0]["plain_text"]

        try:
            # 국내 주식 여부 (네이버 증권)
            price_info = get_naver_price(ticker)

            current_price = price_info["price"]
            change = price_info["change"]
            upanddown = price_info["cr"]
            # 하락이면 음수로 변경
            if price_info["rf"] == "5":
                change = -change
                upanddown = -upanddown

            countOfListedStock = price_info["countOfListedStock"]

            ###################################
            
            # y_finance
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

            # 업데이트 시간 기록
            logger()

            properties = {
                "현재가_깃허브_원본": {
                    "number": current_price
                },
                "전일대비_깃허브": {
                    "number": change
                },
                "등락률_깃허브_원본": {
                    "number": upanddown
                },
                "시가총액_깃허브": {
                    "number": countOfListedStock*current_price
                },
                "52주 최고가": {
                    "number": high_52
                },
                "52주 최저가": {
                    "number": low_52
                },
                "통화": rich_text(currency),
                "국가": rich_text(country),
                "업종": rich_text(sector),
                "산업": rich_text(industry),
                "마지막 업데이트": rich_text(update_time)
            }

            notion.pages.update(
                page_id=page["id"],
                properties=properties
            )

        except Exception as e:
            print(f"❌ {ticker} 오류: {e}")
