from bs4 import BeautifulSoup
import requests
import re

# ------------------------------------------------------------------
# ------------------------------------------------------------------
#   Extracted COT Data 
#   Website: https://www.tradingster.com/cot/legacy-futures
# ------------------------------------------------------------------
# ------------------------------------------------------------------


# Symbol and Links of all data required:
symbol_and_links = [
    {
        "symbol": "EUR",
        "link": "https://www.tradingster.com/cot/legacy-futures/099741"
    },
    {
        "symbol": "USD",
        "link": "https://www.tradingster.com/cot/legacy-futures/098662"
    },
    {
        "symbol": "CAD",
        "link": "https://www.tradingster.com/cot/legacy-futures/090741"
    },
    {
        "symbol": "CHF",
        "link": "https://www.tradingster.com/cot/legacy-futures/092741"
    },
    {
        "symbol": "JPY",
        "link": "https://www.tradingster.com/cot/legacy-futures/097741"
    },
    {
        "symbol": "AUD",
        "link": "https://www.tradingster.com/cot/legacy-futures/232741"
    },
    {
        "symbol": "NZD",
        "link": "https://www.tradingster.com/cot/legacy-futures/112741"
    },
    {
        "symbol": "ZAR",
        "link": "https://www.tradingster.com/cot/legacy-futures/122741"
    },
    {
        "symbol": "GBP",
        "link": "https://www.tradingster.com/cot/legacy-futures/096742"
    },
    {
        "symbol": "GOLD",
        "link": "https://www.tradingster.com/cot/legacy-futures/088691"
    },
    {
        "symbol": "SILVER",
        "link": "https://www.tradingster.com/cot/legacy-futures/084691"
    },
    {
        "symbol": "S&P500",
        "link": "https://www.tradingster.com/cot/legacy-futures/13874%2B"
    },
    {
        "symbol": "UST2Y",
        "link": "https://www.tradingster.com/cot/legacy-futures/042601"
    },
    {
        "symbol": "UST5Y",
        "link": "https://www.tradingster.com/cot/legacy-futures/044601"
    },
    {
        "symbol": "UST10Y",
        "link": "https://www.tradingster.com/cot/legacy-futures/043602"
    },
    {
        "symbol": "NASDAQ-100",
        "link": "https://www.tradingster.com/cot/legacy-futures/20974%2B"
    }
    
]


COT_Percentages = []

# Looping through all links in the list
for i in range(len(symbol_and_links)):
    
    url = symbol_and_links[i]["link"]
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    chart = doc.find(["div"], class_="chart-section")
    table = chart.table
    table_rows = table.find_all(["tr"])
    

    # Ignore the variable "a"
    for tr in table_rows[3:4]:
        long, a, short = tr.contents[1:4]
        
        # Getting rid of commas and converting to int
        long_value = int(long.string.replace(',', ''))
        short_value = int(short.string.replace(',', ''))
        
        long_percentage = ((long_value)/(long_value + short_value))*100
        long_percentage_value = str(round(long_percentage, 2)) + '%'
        
        short_percentage = ((short_value)/(long_value + short_value))*100
        short_percentage_value = str(round(short_percentage, 2)) + '%'
            
        record = {}
        record["symbol"] = symbol_and_links[i]["symbol"]
        record["long_percent"] = long_percentage_value
        record["short_percent"] = short_percentage_value
        
        COT_Percentages.append(record)


    
print(COT_Percentages)



