from datetime import datetime
from zoneinfo import ZoneInfo

def logging():
  update_time = datetime.now(
    ZoneInfo("Asia/Seoul")
  ).strftime("%Y-%m-%d %H:%M")
  return update_time
