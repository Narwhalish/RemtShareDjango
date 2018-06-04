import requests

#zestimate = requests.get("http://www.zillow.com/webservice/GetZestimate.htm?zws-id=X1-ZWz1gfdi9irh1n_1sm5d&zpid=92366643")
#print(zestimate.text)

propertydetails = requests.get("http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=X1-ZWz1gfdi9irh1n_1sm5d&zpid=2089249726
")
print(propertydetails.text)

searchresults = requests.get("http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=<ZWSID>&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA