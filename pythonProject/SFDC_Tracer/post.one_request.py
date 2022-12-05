import requests

transactionId=1409390
publishMetricId=51552

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5MDQyMzk4LCJuYmYiOjE2NjkwNDIzOTgsImV4cCI6MTY2OTA4NTU5OCwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.vPthNydwyLA_Dk5nZ7Fxy1swzRpw2XiY5MB8Fld6JyxnpFNgXmoDR1wT1lF1RrUloX2kvZVdt6Ntje8ShQMl8Vh5Ik9_RAvhIsk_dKeXgGQejUqg8eIACiRP0mx0DLpXwdd92lIK8dYuYXc5AcrwXtcxOjh_K0ewL_wIbgFqZW2PZU_CqyM8zHq75phiNYv89LLbyDzx6bBzNbU_C-cWQtoONuDF_DWUq0elPNkmUHbx1Agyz7ddjnvHxH1lRV3GGwUlc4-Qi--JsoeYPPzYX7PUQ1HVynmQt7CIujckEn7ttbddKGtqYZTqQpKGZe_vY25ioQLI4sKGPt3h8CRRSw"}

endpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

r = requests.get(endpoint, headers=headers)
r_dict = r.json()

argusMetric = r_dict['argusMetric'] ## get argusMetric
tags = argusMetric['tags']          ## get tags within argusMetric
step = tags['step']                 ## get step within tags that is in argusMetric

tagVariables = r_dict['tagVariables']
tag_step = tagVariables[0]['value']

message = f'argusMetric: {argusMetric}\n\ntags: {tags}\n\nstep: {step}\n\ntagVariables:{tagVariables}\n\n'
tag_step_msg = f'tag_step: {tag_step}'
########### POSTING #####
def trace_posting():
    print("===============POSTING====================")
    postpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

    json_payload = r_dict

    r = requests.post(postpoint, headers=headers, json=json_payload)

    print(r.status_code)

##### UPDATES STEPS #####
print("=============")
print("PRINT BEFORE CHANGES")
print("=============")
print(r_dict)

## Delete 2 unwanted
del r_dict['argusExpression']
del r_dict['monexVariable']
del r_dict['publishMetricId']
del r_dict['transactionId']

#steps_list=[1,2,3,4,5,6,7,8]
steps_list=[1]
#locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"]
locations_list=["VIR"]

#########################
def print_msg():
    print(r_dict)
    print("=============")

for step in steps_list:
    r_dict['argusMetric']['tags']['step']=step   ## updated the step
    r_dict['tagVariables'][0]['value']=step
    print(step)
    for location in locations_list: ## updated the step under the tags
        r_dict['argusMetric']['tags']['Location']=location
        r_dict['tagVariables'][1]['value']=location
        print(location)
        print_msg()
        #trace_posting()

#########################
print(len(r_dict['tagVariables']))

for i in r_dict['tagVariables']:
    print(i)