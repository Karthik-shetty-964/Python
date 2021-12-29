import requests

r = requests.get("https://financialmodelingprep.com/education/api-endpoint")
print(r.text)
print(r.status_code)

# Post request
url="www.CodeWithHarry.com"
data={
       'name':'Karthik',
        'age':20
}

r2=requests.post(url=url , data=data)