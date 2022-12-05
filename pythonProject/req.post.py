import requests

payload = {"firstName": "John", "lastName": "Smith"}

r = requests.post("https://httpbin.org/post", data=payload)

print(r.text)
