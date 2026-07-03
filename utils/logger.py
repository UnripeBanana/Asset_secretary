from config import NOTION_DB
from notion.client import notion # notion : 로그인 된 앱에 접근할 수 있도록 해주는 역할
from datetime import datetime
from zoneinfo import ZoneInfo

def logging():
  update_time = datetime.now(
    ZoneInfo("Asia/Seoul")
  ).strftime("%Y-%m-%d %H:%M")
