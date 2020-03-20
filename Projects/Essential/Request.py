import requests

params = {"?#q":"pizza"}

r = requests.get("http://bing.com",params=params)
print("Status:",r.status_code)
print(r.url)
print(r.content)

with open("page.html","w+") as f_obj:
    f_obj.write(r.text)