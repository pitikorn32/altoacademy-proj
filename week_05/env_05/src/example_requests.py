# import requests
# url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network' 
# r = requests.get(url)
# json_data = r.json()
# for key, value in json_data.items():
#       print(key + ':', value)

import requests
# query = "huhu"
# url = f"http://127.0.0.1:5000/?query={query}"
# r = requests.get(url)
# print(r.text)

query = "huhu"
url = f"http://127.0.0.1:5000/route2"
r = requests.post(url, json={"query": query})
print(r.text)