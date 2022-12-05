import requests
import json

headers  = {"content-type": "application/json","Authorization": "Bearer eyJ2ZXJzaW9uIjoiMC4xMSIsImFsZyI6IkhTNTEyIn0.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjU3Mjk2ODcyLCJleHAiOjE2NTczNDAwNzIsInN1YiI6InRhdWxhbnQuc2hhbW8iLCJ0eXBlIjoiQUNDRVNTIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInVzZXJncm91cCI6Ilt7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjMyNjZiZGQ1LWM1ZmEtNGM5Zi05MjNlLTJmN2UyYTc1NzAzNVwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjY4MjI3MTQyLTRhZGUtNGJhMS1iYmE1LTdkZDdkODQyYTNhMlwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjU0ZGYyMGJlLWYyMTEtNDc4Ni1iMjlhLTU3ZjRjZWRiMDhiN1wifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjhmYzY4ZTY1LTRlNTgtNGY5OC04MGFlLTAxNDExMmVkZmE5ZVwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjM5OWE3OTA3LTg5YzUtNGRlNC1iYzEzLTUyNzBiMWQ3ZGU0YVwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjczNGE2Yzg3LTI3YTctNDNmMi04N2FjLTQ3Zjg0YzFlYWRhMlwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjAwZjgxOWM3LTQxMTItNDNjYS05Njg2LWExZWZkYzZlMDhmMlwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjk5OGEyNzFhLTJmZmQtNDM4YS1hNzYwLTY1ODhmZWI1Mjk1NlwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjIwOWM2YjkyLWVmNDEtNDlkOC1iYmQ2LTI0NmM2MmJkNGI3ZlwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjI2NGZiMjhiLTViNzItNDkzMi05MjYzLThiYmMxOGZhYWRkMlwifSx7XCJ1c2VyRGVmYXVsdEdyb3VwR3VpZFwiOlwiXCIsXCJncm91cEd1aWRcIjpcIjA0ODI5NjRkLTU5NTUtNDZjYy1iZmM4LWI0ZmMxYjU5NDQ1ZlwifV0ifQ.jnX1BvlEs82nqCPRKB2W2qDIgAxG-DBvKI3D0OQRuOhFIO7Nj9IW40-YGCz-5WifN0MVVJzjzGxYrJirUfw92w"}
payload = {"derivativeIds": ["63647640"],"startTimestamp": "1653559210000","endTimestamp": "1653568210000"}
#payload = {"derivativeIds": [64069444, 64414973, 64421901, 64421915, 64421916, 64426387, 63647640, 63311027, 63310767, 63311030, 63605360, 63605163, 63647645, 63596603, 63647637, 63657418, 63314485, 63605356, 63605357, 63310768, 63605162, 63302364, 63311026, 63596753, 63606452, 63605161, 64069446, 64069445, 63491058, 63647643, 63314483, 63596751, 63605358, 63605164, 63605474, 63605475, 63489995, 63647639, 63647646, 63310769, 63311031, 63314482, 63314484, 63605359, 63605473, 63490865, 63647644, 63657407, 63596752, 63605361, 63605165, 63647638, 63647642, 63310766, 63311029, 63314481],"startTimestamp": "1653561010000","endTimestamp": "1653568210000"}

url = 'https://monitoring-api.salesforce.com/argusws/derivatives'
#url = 'https://monitoring-api.salesforce.com/argusws/derivatives/backfill'

r = requests.get(url, headers=headers)
#r = requests.put(url, json=payload, headers=headers)

json_data = r.json()
print(json_data)

print(r)
print(r.text)

