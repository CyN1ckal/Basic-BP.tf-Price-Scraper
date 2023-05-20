#Backpack.tf price scraper. Input link into the url and will output the spread between the best buy and sell order.
#It removes buy orders which are above the average sell price, to remove orders for very specific items. IE strange parts, spells, or whatever else.

#The is the very beginning of this script. I plan to do calculation to determine which items are most profitable to trade.

from selenium import webdriver
from classifiedSearch import getPrices
from classifiedSearch import getKSPrices
from calc import spread

path = "C:\\chromedriver.exe"

driver = webdriver.Chrome(executable_path = path)
driver.set_window_size(1000,1000)

#getPrices(driver,"https://next.backpack.tf/classifieds?spell=none&texture=none&quality=11&first=0&rows=10&festivized=0&australium=1&itemName=Ambassador&killstreakTier=3")
#spread(test)

#Iterates through all version of the killstreak weapon linked.
getKSPrices(driver,'https://next.backpack.tf/classifieds?spell=none&texture=none&quality=11&first=0&rows=10&festivized=0&killstreakTier=3&itemName=Festive%20Knife')