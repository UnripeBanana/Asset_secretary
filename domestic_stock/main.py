from domestic_stock.read import get_ticker
from domestic_stock.update import update_stock_DB
from data.domestic_stock import get_naver_prop, get_yfinance_prop

def domestic_stock_main(pages)
  for page in pages:
  
    ticker = get_ticker(page)
    
    stock_info = {
        **get_naver_prop(ticker),
        **get_yfinance_prop(ticker)
    }
  
    update_stock_DB(stock_info)
