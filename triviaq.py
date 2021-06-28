import requests

# Some examples of requests that can be used: GET, POST, PUSH, PUT, DELETE, PATCH

url= "https://opentdb.com/api.php?amount=1&category=15&difficulty=easy&type=boolean"

resp= requests.get(url)

print(dir(resp))

x= resp.json()

#print(html.unescape(x["results"][0]["question"]))

print(type(x))

#dump a json object into a python "string"

x= json.loads(x)

print(type(x))
