#Checks whether the price is in refined or keys and returns a dictionary with the value.
def getcurrency(listingprice):
    currency = {'ref': 0, 'keys': 0}
    if (listingprice.text.find(' ref') >= 0):
        currency['ref'] = float(listingprice.text.replace(' ref', ''))
        return currency
    elif (listingprice.text.find(' keys') >= 0):
        currency['keys'] = float(listingprice.text.replace(' keys', ''))
        return currency
    elif (listingprice.text.find(' key') >= 0):
        currency['keys'] = float(listingprice.text.replace(' key', ''))
        return currency
    else:
        print("Other")