from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from currency import getcurrency
import statistics
from calc import spread
def getPrices(driver,url):

    #This is the main function so far. Gets prices from backpack.tf and returns them.

    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/div[1]")))
    except:
        print("Exception")

    selling = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/div[1]")   #Seperating buy classified column
    buying = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div[3]/div[2]")    #from the sell classified column

    sellElements = selling.find_elements(By.CLASS_NAME, "item__price")  #Finding all individual sell orders within the selling column
    buyElements = buying.find_elements(By.CLASS_NAME, "item__price")    #Finding all individual buy orders within the buying column

    sellPrices = []     #Declaring empty array for later
    buyPrices = []      #Declaring empty array for later
    temp = []           #For calculating avg later


    for i in sellElements:
        curorder = getcurrency(i)               #Parses price information from the element
        if (curorder == 0):
            continue
        sellPrices.append(curorder)
        temp.append(curorder.get('keys'))       #For calculating avg later
    avgsell = statistics.mean(temp)             #For calculating avg


    for i in buyElements:
        curorder = getcurrency(i)       #Parses price information from the element
        if (curorder == 0):
            continue
        if(curorder.get('keys')>avgsell):       #If current buy order is above average price, skip it.
            continue                            #Reason is to avoid pricing the expensive "one-offs"/spells orders
        buyPrices.append(curorder)

    print(sellPrices)
    print(buyPrices)
    return sellPrices,buyPrices

def getKSPrices(driver,url):
    for i in range(4):
        url = url[:url.index('killstreakTier=') + 15], str(i), url[url.index('killstreakTier=') + 16:]
        url = ''.join(url)
        spread(getPrices(driver,url))