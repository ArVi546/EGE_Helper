import requests

link = "https://ege.fipi.ru/bank/"

response = requests.get(link)
print(response.status_code)
print(response.headers.get("content-type"))