from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# ------------------------------------------------------------------
# ------------------------------------------------------------------
#   Extracted Interest Rates of Different Countries
#   Website: https://tradingeconomics.com/euro-area/interest-rate
# ------------------------------------------------------------------
# ------------------------------------------------------------------


# Symbol and Links of all data required:
country_symbol_and_links = [
    {
        "country": "United States",
        "symbol": "USD",
        "link": "https://tradingeconomics.com/united-states/interest-rate"
    },
    {
        "country": "European Central Bank",
        "symbol": "EUR",
        "link": "https://tradingeconomics.com/euro-area/interest-rate"
    },
    {
        "country": "Canada",
        "symbol": "CAD",
        "link": "https://tradingeconomics.com/canada/interest-rate"
    },
    {
        "country": "Japan",
        "symbol": "JPY",
        "link": "https://tradingeconomics.com/japan/interest-rate"
    },
    {
        "country": "New Zealand",
        "symbol": "NZD",
        "link": "https://tradingeconomics.com/new-zealand/interest-rate"
    },
    {
        "country": "Australia",
        "symbol": "AUD",
        "link": "https://tradingeconomics.com/australia/interest-rate"
    },
    {
        "country": "United Kingdom",
        "symbol": "GBP",
        "link": "https://tradingeconomics.com/united-kingdom/interest-rate"
    },
    {
        "country": "Switzerland",
        "symbol": "CHF",
        "link": "https://tradingeconomics.com/switzerland/interest-rate"
    },
    {
        "country": "South Africa",
        "symbol": "ZAR",
        "link": "https://tradingeconomics.com/south-africa/interest-rate"
    }
]

Country_Interest_Rates = []


# Looping through all links in the list
for i in range(len(country_symbol_and_links)):

    options = Options()
    options.add_argument('--headless')

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path, options=options)

    url = country_symbol_and_links[i]["link"]
    symbol = country_symbol_and_links[i]["symbol"]
    driver.get(url)

    wait = WebDriverWait(driver, 10)    
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))


    page_source = driver.page_source
    doc = BeautifulSoup(page_source, "html.parser")


    # ----------------------------------------
    # Interest Rate - Extracting
    # ----------------------------------------

    entire_div = doc.find(["div"], id="ctl00_ContentPlaceHolder1_ctl00_ctl02_Panel1")

    trows = entire_div.tbody.tr

    td_list = trows.find_all("td")

    actual_interest_rate = td_list[1].string
    previous_interest_rate = td_list[2].string

    record = {}
    record["symbol"] = symbol
    record["actual_interest_rate"] = actual_interest_rate
    record["previous_interest_rate"] = previous_interest_rate

    Country_Interest_Rates.append(record)
   
print(Country_Interest_Rates)
