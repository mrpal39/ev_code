import http.client

conn = http.client.HTTPSConnection("bloomberg-market-and-financial-news.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "bd689f15b2msh55122d4390ca494p17cddcjsn225c43ecc6d4",
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

conn.request("GET", "/market/get-cross-currencies?id=aed%2Caud%2Cbrl%2Ccad%2Cchf%2Ccnh%2Ccny%2Ccop%2Cczk%2Cdkk%2Ceur%2Cgbp%2Chkd%2Chuf%2Cidr%2Cils%2Cinr%2Cjpy%2Ckrw%2Cmxn%2Cmyr%2Cnok%2Cnzd%2Cphp%2Cpln%2Crub%2Csek%2Csgd%2Cthb%2Ctry%2Ctwd%2Cusd%2Czar", headers=headers)

res = conn.getresponse()
data = res.read()


    # print(data.decode("utf-8"))
print(data.json())