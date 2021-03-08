import requests
import json

url='https://www.scraping-bot.io/rawHtmlPage.html'
username = 'yourUsername'
apiKey = 'yourApiKey'

apiUrl = "http://api.scraping-bot.io/scrape/raw-html"

payload = json.dumps({"url":url})
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", apiUrl, data=payload, auth=(username,apiKey), headers=headers)

print(response.text)



import requests
import json

url='https://www.scraping-bot.io/rawHtmlPage.html'
username = 'yourUsername'
apiKey = 'yourApiKey'

apiEndPoint = "http://api.scraping-bot.io/scrape/raw-html"

options = {
    "useChrome": False,#set to True if you want to use headless chrome for javascript rendering
    "premiumProxy": False, # set to True if you want to use premium proxies Unblock Amazon,Google,Rakuten
    "proxyCountry": None, # allows you to choose a country proxy (example: proxyCountry:"FR")
    "waitForNetworkRequests":False # wait for most ajax requests to finish until returning the Html content (this option can only be used if useChrome is set to true),
                                   # this can slowdown or fail your scraping if some requests are never ending only use if really needed to get some price loaded asynchronously for example
}

payload = json.dumps({"url":url,"options":options})
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", apiEndPoint, data=payload, auth=(username,apiKey), headers=headers)

print(response.text)

 https://libraries.io/api/NPM/base62?api_key=306cf1684a42e4be5ec0a1c60362c2ef 
import requests
import json

url='https://www.scraping-bot.io/example-ebay.html'
username = 'yourUsername'
apiKey = '306cf1684a42e4be5ec0a1c60362c2ef'

apiEndPoint = "http://api.scraping-bot.io/scrape/retail"

payload = json.dumps({"url":url,"options":options})
headers = {
    'Content-Type': "application/json"
}

response = requests.request("POST", apiEndPoint, data=payload, auth=(username,apiKey), headers=headers)

print(response.text)