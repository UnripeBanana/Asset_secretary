from gold.update import update_KRX_GOLD_INFO_DB
from data.domestic_gold import get_gold_price

def gold_main (pages):
  for page in pages:
    gold_info = get_gold_price()
  
    update_KRX_GOLD_INFO_DB(page, gold_info)

"""
  "price": int(gold["closePrice"].replace(",", "")),           # 현재가
  "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
  "rate": float(gold["fluctuationsRatio"]),                    # 등락률
  "direction": gold["fluctuationsType"]["name"]                # 등락여부
"""
