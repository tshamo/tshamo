import requests

payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()

print(r_dict)
print(r_dict['form'])
