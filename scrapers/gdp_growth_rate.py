from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# ------------------------------------------------------------------
# ------------------------------------------------------------------
#   Extracted European Union GDP & GDP Growth Rate
#   Website: https://tradingeconomics.com/european-union/gdp
# ------------------------------------------------------------------
# ------------------------------------------------------------------


# Preventing Window from opening
options = Options()
options.add_argument('--headless')


# Driver
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path, options=options)

url = "https://tradingeconomics.com/european-union/gdp"
driver.get(url)

# Waiting for Page Load (Waits 10 second until the tag <tbody> is loaded)
wait = WebDriverWait(driver, 10)    
wait.until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))

# Page Source
page_source = driver.page_source

# Parse HTML with BeautifulSoup
doc = BeautifulSoup(page_source, "html.parser")


# ----------------------------------------
# GDP Growth Rate - Extracting
# ----------------------------------------

tbody = doc.tbody
trows = tbody.contents

# Data List
European_Union_GDP_dataset = []


# Below the <tr> object you are trying to call the find_all() method on is actually a NavigableString object, not a Tag object.
for tr in trows:
    
    # check if the row is a tag object
    if tr.name == 'tr':
        columns = tr.find_all('td')
        related, last, previous, unit, reference = columns[0], columns[1], columns[2], columns[3], columns[4]
        
        # New Dictionary for each Record
        record = {}
        record["related"] = related.text.strip()
        record["last"] = last.text.strip()
        record["previous"] = previous.text.strip()
        record["unit"] = unit.text.strip()
        record["reference"] = reference.text.strip()
        
        European_Union_GDP_dataset.append(record)


# The required data value was "GDP Growth Rate"
GDP_Growth_Rate = European_Union_GDP_dataset[4]

print(European_Union_GDP_dataset)
print()
print()
print(GDP_Growth_Rate)


