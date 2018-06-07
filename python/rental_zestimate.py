import requests

def rental_zestimate(url, zipcode):
    one = url.index(zipcode +"/")+6
    two = url.index("_zpid")
    url = url[one:two]
    response = requests.get("http://www.zillow.com/webservice/GetZestimate.htm?zws-id=X1-ZWz1gfdi9irh1n_1sm5d&zpid="+url+"&rentzestimate=true")
    return(response.content)
    
def parse_zestimate(response):
    