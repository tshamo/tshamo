import requests


publishMetricId=51552
transactionId=1409390

page = 'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/1409390/publish-metrics/51552'

r = requests.get(page)

print(r.status_code)
print(r.ok)
print(r.headers)
print(r.url)