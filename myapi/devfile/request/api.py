# import requests
# url = "https://proxy-orbit1.p.rapidapi.com/v1/"
# headers = {
#     'x-rapidapi-key': "b188eee73cmsha4c027c9ee4e2b7p1755ebjsn1e0e0b615bcf",
#     'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com"
#     }
# # response = requests.request("GET", url, headers=headers)
# print(response.text)

import requests
url= "https://libraries.io/api/"
headers={'?api_key':'306cf1684a42e4be5ec0a1c60362c2ef',
# 'platform':'NPM/base62/dependent_repositories'
}
response = requests.request("GET", url, headers=headers)
print(response.text)





Example: https://libraries.io/api/NPM/base62/dependent_repositories?api_key=306cf1684a42e4be5ec0a1c60362c2ef 











import requests

url = "https://scrapingant.p.rapidapi.com/post"

payload = "{\"cookies\": \"cookie_name_1=cookie_value_1;cookie_name_2=cookie_value_2\"\"return_text\": false,\"url\": \"https://example.com\"}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "b188eee73cmsha4c027c9ee4e2b7p1755ebjsn1e0e0b615bcf",
    'x-rapidapi-host': "scrapingant.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


