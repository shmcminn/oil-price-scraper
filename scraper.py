import json

import requests
import pandas as pd 
# import gspread
# from df2gspread import df2gspread as d2g
# from google.oauth2.service_account import Credentials



url = "https://markets.businessinsider.com/Ajax/Chart_GetChartData?instrumentType=Commodity&tkData=300002,6,0,333&from=20220201&to=20290309"

resp = requests.get(url)

json_data = json.loads(resp.text)

df = pd.DataFrame(json_data)

df = df[['Close', 'Date']]

  
# calculating simple moving average
# using .rolling(window).mean() ,
# with window size = 30
new_col_name = "5-day average"
df[new_col_name] = df['Close'].rolling(5).mean()
  
# removing all the NULL values using 
df = df[df[new_col_name].isnull() == False]

print(df)












# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']

# credentials = Credentials.from_service_account_file(
#     '/Users/smcminn/Documents/graphics/oil-scraper/kinetic-anvil-183322-c22d5c1be305.json',
#     scopes=scope
# )

# gc = gspread.authorize(credentials)

# spreadsheet_key = '1rZCwg40DSjqjEv-TrAihO7Z4s64JUhkF2Cyxoa1z7Uw'



# sh = gc.open_by_key(spreadsheet_key)
# worksheet = sh.get_worksheet(0)

# worksheet.clear()

# worksheet.update([df.columns.values.tolist()] + df.values.tolist())

df.to_csv("oil-prices.csv", index=0)

