

for page in get_all_pages(DATABASE_ID):

  props = page["properties"]

  ticker_data = props["티커"]["rich_text"]

  if len(ticker_data) == 0:
      continue

  ticker = ticker_data[0]["plain_text"]
