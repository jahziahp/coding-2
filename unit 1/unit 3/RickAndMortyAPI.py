import requests

url = 'https://rickandmortyapi.com/api/character/1'
response = requests.get(url)
print(response.status_code)
print(response.json)

if status == 200:
    data = res.json()
    filterData = {
        "name":data['name'],
        "status":data["status"],
        "image":data["iamge"],
    }

    print(filterdata)
else:
    print("somthing went wrong")
    print(res.status_code)