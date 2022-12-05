import requests

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey','testing'), timeout=3)

print(r.text)
print(r)
print(r.ok)
print(r.status_code)

