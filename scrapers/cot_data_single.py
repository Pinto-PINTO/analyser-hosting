from bs4 import BeautifulSoup
import requests
import re


# ------------------------------------------------------------------
# ------------------------------------------------------------------
#   Extracted COT Data from Single Website
#   Website: https://www.tradingster.com/cot/legacy-futures
# ------------------------------------------------------------------
# ------------------------------------------------------------------

# Enter URL of single website
# GBP COT Data
url = "https://www.tradingster.com/cot/legacy-futures/096742"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")


chart = doc.find(["div"], class_="chart-section")
table = chart.table
table_rows = table.find_all(["tr"])


COT_Data_Single_Percentages = []



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
    record["symbol"] = 'GBP'
    record["long_percent"] = long_percentage_value
    record["short_percent"] = short_percentage_value
    
    COT_Data_Single_Percentages.append(record)


print(COT_Data_Single_Percentages)
