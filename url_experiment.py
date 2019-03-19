import urllib
import http

def unshorten_url(url):
    parsed = urllib.parse(url)
    h = http.client(parsed.netloc)
    resource = parsed.path
    if parsed.query != "":
        resource += "?" + parsed.query
    h.request('HEAD', resource )
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return unshorten_url(response.getheader('Location')) # changed to process chains of short urls
    else:
        return url
    
ooo=unshorten_url('https://t.co/YYXyjnIEbv')

import requests
r = requests.head('https://t.co/YYXyjnIEbv', allow_redirects=True)
print(r.url)
import requests
r = requests.head('https://t.co/YYXyjnIEbv', allow_redirects=True)
print(r.url)

domain=r.url.split(“//”)[-1].split(“/”)[0]
print domain
import re

domain=r.url.split(“//”)[-1].split(“/”)[0]
print domain
r.url.split('/')[2]
r.url.split('/')[0]
r.url.split('/')[1]
r.url.split('/')[2]

domain=r.url.split('//')[-1].split('/')[0]
print domain

domain=r.url.split('//')[-1].split('/')[0]
print (domain)