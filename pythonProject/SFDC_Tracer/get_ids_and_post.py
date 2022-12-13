import requests
from wipMethGet import getMetricSeriesIds
from wipMethGet import getReplaceablesIds
from wipMethGet import parseJSON
from wipMethGet import post_payload
from wipMethGet import getKaijuTestId
from wipMethGet import validate_input
from wipMethGet import confirm_prompt


transactionId = 1445340
#testId = 43901


pod_list = ["gs0"]
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"]

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjcwOTQ0MjQzLCJuYmYiOjE2NzA5NDQyNDMsImV4cCI6MTY3MDk4NzQ0MywiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.FxN8DJMQyi15tKxowR7a6jD0SzNwRHdLEEoWJZnARzOIAUmqu97zCTEV1mG4EF7rPMsy_wqozXY6v5OQTAumjgMMGAZtUZVMjSDjYOPzfx3MihcpWSOCxo9BMPHNw3j5R0xYCabMKhHKyZkvlF71bLH4Gn6KwdpJxcrXowr8to1YTmnGGBm2OgJZUkAGlJ2dY5FJqa1i2xmeYll8acZPJIiQiKfJREixxOXlgeBgXkiIdZ4LCwgQ6I9O8xIk0slTXkzpucz_apRzdp420qZD0p8OOQTeEXaRbjaERWwXy3usm7OL5vZRshVJ4I8hGG84No4FLblw6ZiSQALr7X3LrQ"}
endpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}'

r = requests.get(endpoint, headers=headers)
r_dict = r.json()
json_payload = r_dict


available_metrics = ["http_avg", "db-sql", "cache", "soql"]

# Get metrics to Publish Metrics
input_string = input(f"Enter seriesName. Valid options are {available_metrics}: ")
input_list = input_string.split()
print(input_list)

# Validate input metrics - if input metrics are NOT in available_metrics stop running, otherwise run
validate_input(input_list, available_metrics)

## Get Kaju testId
kaiju_testId = getKaijuTestId(json_payload)
print(f'kaiju_testId: {kaiju_testId}')

print(f'transactionId: {transactionId}')

### Get Replaceable Ids
replaceablesIds = getReplaceablesIds(json_payload)
print(replaceablesIds)

### Get metric Ids
id_seriesId_dict = getMetricSeriesIds(json_payload)
print(id_seriesId_dict)

pod_id = replaceablesIds["pod"]
Location_id = replaceablesIds["Location"]
testId_id = replaceablesIds["testId"]

#print(f'Replaceable IDS: pod_id={pod_id}, Location_id={Location_id}, testId:_id={testId_id}')

print(f'Pod list: {pod_list}')
print(f'Location list: {locations_list}')

## Final confirmation
reply = confirm_prompt("Do you want to proceed?")

for metric in input_list:
    metricName = metric
    seriesName = metric
    seriesId = id_seriesId_dict[metric]
    ## parse JSON
    parsed_json = parseJSON(seriesId, seriesName, metricName, transactionId, pod_id, Location_id, testId_id, kaiju_testId)
    #print(f'Metric IDS: metricName={metricName}, seriesName={seriesName}, seriesId={seriesId}, transactionId={transactionId}')

    for pod in pod_list:
        parsed_json['argusMetric']['tags']['pod'] = pod
        parsed_json['tagVariables'][0]['value'] = pod

        for location in locations_list:
            parsed_json['argusMetric']['tags']['Location'] = location
            parsed_json['tagVariables'][1]['value'] = location
            #print(pod, location, metricName)
            print(parsed_json)
            ## Uncomment below line to post parsed_json
            #post_payload(transactionId, headers, parsed_json)