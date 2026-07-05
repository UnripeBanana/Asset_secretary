# 노션에 쓰는 함수만 넣는다.

from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from notion.rich_text import rich_text
from utils.logger import logging
from config import NOTION_KRX_GOLD_INFO_DB_ID

def update_KRX_GOLD_INFO_DB(page, gold_info):

  price = gold_info["price"]
  change = gold_info["change"]
  rate = gold_info["rate"]
  direction = gold_info["direction"]
  
  # 하락이면 음수로 변경
  if direction == "FALLING":
    change = -change
    rate = -rate
  elif direction == "UNCHANGED":
    change = 0
    rate = 0

  gold_info_mod = {
    "현재가_깃허브_원본": {
        "number": price
    },
    "전일대비_깃허브_원본": {
        "number": change
    },
    "등락률_깃허브_원본": {
        "number": rate
    },
    "마지막 업데이트": rich_text(logging())
  } 
    
  notion.pages.update(
      page_id=page["id"],
      properties=gold_info_mod
  )
