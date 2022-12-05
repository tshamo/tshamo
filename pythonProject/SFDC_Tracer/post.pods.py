import requests

json_payload = {
            "seriesId": 1402075,
            "seriesName": "soql",
            "metricType": "avg",
            "frequencyMin": 10,
            "lookbackMin": 10,
            "delayMin": 10,
            "argusMetric": {
                "metricName": "soql",
                "service": "tracer",
                "subService": "",
                "dataCenter": "PRD",
                "superPod": "NONE",
                "pod": "none",
                "tags": {
                    "pod": "eu18",
                    "seriesName": "soql",
                    "testId": "43901",
                    "transactionId": "1419102",
                    "Location": "SYD"
                }
            },
            "tagVariables": [
                {
                    "id": 2820489,
                    "name": "Location",
                    "value": "SYD"
                },
                {
                    "id": 2820491,
                    "name": "pod",
                    "value": "eu18"
                },
                {
                    "id": 2820490,
                    "name": "testId",
                    "value": "43901"
                }
            ]
        }

transactionId=1420704

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5MjE5MTIzLCJuYmYiOjE2NjkyMTkxMjMsImV4cCI6MTY2OTI2MjMyMywiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.CUPfeRdk7P7IORsvzYorTDVIOo6wDeBnt4MHG75GetfAZAa1nJ2FR0jLlG23gS8eDTccdqdPE6Ptj4G05kEZ-Xwu3t2Ph9PtwD-bQQvcgPi_Uh9vTERuNo9mD-cN7GwrPBk2MNu9NCCLfGPEwKkO6SisvfCmplfMTLZO9aC790RXY0o_iuKHwlKMFYyBeA36Ju2yOtzaKPY4jCfOjBZTqs8izwXvez6yedD8kjLdG7rPEamhUqXmmCf91N8ugcM8u2BB7Eyds8MuS6NrUT8Gk01KR2wU0e_JxYVD20K-s39zk-PibhtqoyUPHiI23mHnfKz6tJjpETu9GyqHeL0ngQ"}

argusMetric = json_payload['argusMetric'] ## get argusMetric
tags = argusMetric['tags']          ## get tags within argusMetric
pod = tags['pod']                 ## get step within tags that is in argusMetric

tagVariables = json_payload['tagVariables']
pod_step = tagVariables[1]['value']

message = f'argusMetric: {argusMetric}\n\ntags: {tags}\n\npod: {pod}\n\ntagVariables:{tagVariables}\n\n'
tag_step_msg = f'tag_step: {pod_step}'
########### POSTING #####
def trace_posting():
    print("===============POSTING====================")
    postpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

    r = requests.post(postpoint, headers=headers, json=json_payload)

    print(r.status_code)

##### UPDATES STEPS #####
print("=============")
print("PRINT BEFORE CHANGES")
print("=============")
print(json_payload)

locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"]
pod_list=["eu10","eu11","eu11","eu12","eu14","eu15","eu17","eu18","eu19"]

#########################
def print_msg():
    print(json_payload)
    print("=============")

for pod in pod_list:
    json_payload['argusMetric']['tags']['pod']=pod
    json_payload['tagVariables'][1]['value']=pod
    print(pod)
    for location in locations_list: ## updated the step under the tags
        json_payload['argusMetric']['tags']['Location']=location
        json_payload['tagVariables'][0]['value']=location
        print(location)
        print_msg()
        trace_posting()

#########################

print(len(json_payload['tagVariables']))

for i in json_payload['tagVariables']:
    print(i)