from domestic_gold.update import update_KRX_GOLD_INFO_DB
from data.domestic_gold import get_gold_price

def gold_main (pages):
  for page in pages:
    
    stock_info = {
        **get_gold_price(ticker),
    }
  
    update_stock_DB(page, stock_info)

"""
  "price": int(gold["closePrice"].replace(",", "")),           # 현재가
  "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
  "rate": float(gold["fluctuationsRatio"]),                    # 등락률
"""
