import json
import requests

 
def image_search(query, amount=1):
#returns 'amount' number of query results in a list. 
    results = []
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + query + '&start=%d'
    start = 0 # Google's start query string parameter for pagination.
    while start < amount: # Google will only return a max of 56 results.
        r = requests.get(BASE_URL % start)
        for image_info in json.loads(r.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            results.append(url)
            start +=1

    return results[:amount]


def embeddable_image(query, amount=1):
#returns 'amount' number of 
    results = []
    for image in image_search(query,amount):
        results.append('<img src = "{0}>'.format(image))

    return results
