import requests

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY4Nzg5OTA0LCJuYmYiOjE2Njg3ODk5MDQsImV4cCI6MTY2ODgzMzEwNCwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.YFadNeiyFCxCCebkPIwlE-CJLDxH2xuPGsm6jT_yZhFihozzTv40PqeLG4l-GSEHAfEQFc-foCFX8n1AZvqaD5tCLDoT0IPTC6irQ7JeYO3mbXPtetgs38i12GpDiv-Q1sLurxpLEgnx86neDzi_xb_UgV6tMXDxltZYqa89J3Wvbv_-VE1P1o_noFhQjinuoH6xFJAmvo4VogC7mPugBM7hFYw2ThiGnOY_PR2lpXt6SSs-fZSmmKSEFNuDPn94Ah_sV0uPMNQ79eX9igiiGoeohkcHr8D-2rO_H__9zqx0WCDfNzqw_roBT53Y3FObG9NA_P7Qc4q0IS1IhLQDgw"}

#endpoint = "https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/1409390/publish-metrics/51552"
endpoint = "https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/1409390/publish-metrics"

r = requests.get(endpoint, headers=headers).json()

'''
publishMetricId=r['publishMetricId']
transactionId = r['transactionId']
seriesId = r['seriesId']
seriesName = r['seriesName']
metricType = r['metricType']
argusMetric = r['argusMetric']
metricName = argusMetric['metricName']
service = argusMetric['service']
tags = argusMetric['tags']
step = tags['step']
testId = tags['testId']
tagVariables = r['tagVariables']

l1=tagVariables[0]
l2=tagVariables[1]

#print(f'publishMetricId:{publishMetricId},\ntransactionId:{transactionId},\nseriesId:{seriesId},\nseriesName:{seriesName},\nmetricType:{metricType},\nmetricName:{metricName},\nservice:{service},\ntags:{tags},\nstep:{step},\ntestId:{testId},\ntagVariables:{tagVariables}')
#print(f'l1:{l1},\nl2:{l2}')

for i in tagVariables:
    for kj,vj in i.items():
        print(f'{kj}:{vj},')
    #print(i)


for key, value in r.items():
    print(key, value)
'''

publishMetrics=r['publishMetrics']
#publishMetricId=publishMetrics['publishMetrics']

for i in publishMetrics:
    dic=i
    for k,v in dic.items():
        dic1 = {}
        if (k == 'publishMetricId' or k == 'transactionId'):
            #dic1[k].append(v)
            publishMetricId=v
            transactionId=v
            print(k, v)
            print(f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics/{publishMetricId}')
        #print(k,v)
        #print(dic1)
    #print (f'{i}\n')

print("\n")
#print(r)

