# Basic-BP.tf-Price-Scraper

Very basic selenium webscraper. The goal of this scraper is to get a list of all classifieds (both buy and sell) and put the data into an array for later analyzing. 

Change the URL to the classifieds page of your choosing, and run the program. It will find all item_price elements and put them into their respective array for either buy or sell orders. 

So far there are 2 "filters." 
Firstly, I only look at prices that are in refined, or ref. This scraper is only to be used on items priced in refined. 
Secondly, I remove any buy orders which are above the mean sell order price. This is to remove any high buy order for a specific variant; aka lvl 100s, spelled, etc.

As of now all the program does it output both arrays and the spread between the best sell and buy order.
