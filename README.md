# Basic-BP.tf-Price-Scraper

Very basic selenium webscraper. The goal of this scraper is to get a list of all classifieds (both buy and sell) and put the data into an array for later analyzing. 

Change the URL to the classifieds page of your choosing, and run the program. It will find all item_price elements and put them into their respective array for either buy or sell orders. 

I remove any buy orders which are above the mean sell order price. This is to remove any high buy order for a specific variant; aka lvl 100s, spelled, etc.

As of now all the program does is print both arrays and the spread between the best sell and buy order.
