import requests
import json

headers = {"content-type": "application/json","Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZXhwIjoxNjU4MzUwMzc3LCJpYXQiOjE2NTgzNDY3Nzd9.um1xxvithZXYyTGgA17qgU5qpzlFRm_sDyv0qM5fWqxhrPmLC4WboAFbX-L5_OmNXTcHZ4NJAAEZCAhf_09dMA"}

#url = 'https://monitoring-api.salesforce.com/argusws/derivatives/backfill'
url = 'https://monitoring-api.salesforce.com/argusws/derivatives'

payload = {
	"derivativeIds": ["63725740","63725075","63726079","63726216","63725961","63726218","65082911","65082769","65082770","65082771","65082772","65083194","63725076","63726217","64863985","64863986","64863987","64864522","64865492","64865493","63725737","63725736","63726164","63726078","63726215","63726080","63725738","63725739","63725074","63726163"],
	"startTimestamp": "1659607286486",
	"endTimestamp": "1659632160205"
}

#r = requests.put(url, headers=headers, data=payload)
#r = requests.put(url, headers=headers, json=payload)
r = requests.get(url, headers=headers)

print(r.text)