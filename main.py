#Backpack.tf price scraper. Input link into the url and will output the spread between the best buy and sell order.
#It removes buy orders which are above the average sell price, to remove orders for very specific items. IE strange parts, spells, or whatever else.

#The is the very beginning of this script. I plan to do calculation to determine which items are most profitable to trade.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import statistics
from time import sleep
path = "C:\\chromedriver.exe"
url = "https://next.backpack.tf/classifieds?spell=none&texture=none&quality=11&killstreakTier=0&australium=0&first=0&rows=10&festivized=0&itemName=Knife"

driver = webdriver.Chrome(executable_path = path)

driver.get(url)



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/div[1]"))
    )
except:
    print("Exception")

selling = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/div[1]")
buying = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/div[2]")

sellelements = selling.find_elements(By.CLASS_NAME, "item__price")
buyelements = buying.find_elements(By.CLASS_NAME, "item__price")

sellPrices = []
buyPrices = []

for i in sellelements:
    if(i.text.find("ref") == -1):
        continue
    curorder = float(i.text.replace(' ref', ''))
    sellPrices.append(curorder)

for i in buyelements:
    if(i.text.find("ref") == -1):
        continue
    curorder = float(i.text.replace(' ref', ''))
    if(curorder > statistics.mean(sellPrices)):
        continue
    buyPrices.append(curorder)

print(sellPrices)
print(buyPrices)
print("The Spread is ", sellPrices[0]-buyPrices[0])



