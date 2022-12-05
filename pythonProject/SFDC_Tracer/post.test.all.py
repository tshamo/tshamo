import requests
'''
!!!! Generates and posts metrics for tracer !!!!
This works fine. It is ugly, buy works :)
'''
def set_variables():
    headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5OTA2MTkyLCJuYmYiOjE2Njk5MDYxOTIsImV4cCI6MTY2OTk0OTM5MiwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.hAW8r8PTY76xlxRXJB_GilZaq2uTjsTYt7CmsJR_IIkFEQmorBPXod4wIilb1Fs6t88wfuR7ALGAnY-y70H8lP0PLJJYq5lPVj685rwMPNcG9nCc1gHsqK0dRrdXj8DOKA5nPSq_nnHwVHWGSCJPlhytr7yLNxjIOupG8mmKaaOkMrNO9sYhTjWAXXcsQ4xw40tj7ivteg-tMCJY6zARfgHp8oAfsmT8ULd_nYzO1NNz7prWD3NtsuzBs2Hsm09MfzTb2ufOH4dkUInx6jpZwL8g_y7sEuRTkqF0stcmRFC5JwCGPdA_iqLzpKke8TwtMSUuxyabLd9iJU0msWg5Qg"}

    transactionId=1436021
    pod_list=["cs101"]
    locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"]
    steps_list=[1,2,3,4,5,6,7,8]

# Validate the metric entered
valid_metric_list = ["root","http_resp","cache","db-sql","soql"]

def valid_metric_check(prompt):
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print("Sorry, that is not a valid metric.")
            continue

        if value not in valid_metric_list:
            print("Sorry, that is not a valid metric. Valid list is", valid_metric_list)
            continue
        else:
            break
    return value

metric = valid_metric_check("Enter metric: ")

# Set defaults depending on the metric entered
metrics_var = {'root':{"seriesId": 0},'http_resp':{"seriesId": 1422556},'db-sql':{"seriesId": 1422557},'cache':{"seriesId": 1422558},'soql':{"seriesId": 1422559} }

def set_metric_defaults(*args):
    seriesId = 0
    seriesName = ""
    metricName = seriesName

    for arg in args:
        seriesName = arg
        for k, j in metrics_var[arg].items():
            seriesId = j
            seriesName = arg
            print(seriesName, seriesId)
    return seriesName, seriesId

m_defaults = set_metric_defaults(metric)
#print(m_defaults)

seriesId = m_defaults[1]
seriesName = m_defaults[0]
metricName = seriesName

print(seriesId,seriesName, metricName)

json_payload = {
            "seriesId": seriesId,
            "seriesName": seriesName,
            "metricType": "avg",
            "frequencyMin": 10,
            "lookbackMin": 10,
            "delayMin": 10,
            "argusMetric": {
                "metricName": metricName,
                "service": "tracer",
                "subService": "",
                "dataCenter": "PRD",
                "superPod": "NONE",
                "pod": "none",
                "tags": {
                    "pod": "ap11",
                    "seriesName": seriesName,
                    "testId": "43901",
                    "transactionId": transactionId,
                    "Location": "TYO"
                }
            },
            "tagVariables": [
                {
                    "id": 2845986,
                    "name": "pod",
                    "value": "ap11"
                },
                {
                    "id": 2845984,
                    "name": "Location",
                    "value": "TYO"
                },
                {
                    "id": 2845985,
                    "name": "testId",
                    "value": "43901"
                }
            ],
            "argusExpression": "-1h:tracer.PRD.NONE.none:tracer_http_resp_avg{pod=ap11,seriesName=http_resp,testId=43901,transactionId=1435693,Location=TYO}:avg:1m-avg",
            "monexVariable": "test"
        }

print("This will be your json payload file\n----------------------------------------")
print (json_payload)



######################### LAST CONFIRMATION TO PROCEED ##################

def confirm_prompt(question, default="n"):
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").lower()
        if reply == "n":
            print("exiting")
            exit()
        elif reply == "y":
            print("Running....")
        else:
            confirm_prompt("That is not a valid option. Enter")
    return (reply == "y")
print()
reply = confirm_prompt("Do you want to proceed?")

# Generate JSON Payload dynamically

'''def generate_payload(json_payload):
    del json_payload['argusExpression']
    del json_payload['monexVariable']

    argusMetric = json_payload['argusMetric']'''


########### POSTING #####
def trace_posting():
    print("===============POSTING====================")
    print(json_payload)
    postpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

    r = requests.post(postpoint, headers=headers, json=json_payload)

    print(r)

#########################

def print_msg():
    print(json_payload)
    print("+++++++++++++++++++++++++")
#########################
def prepare_json():
    for pod in pod_list:
        json_payload['argusMetric']['tags']['pod']=pod   ## updated the step
        json_payload['tagVariables'][0]['value']=pod
        #print(pod)
        for location in locations_list:  ## updated the step under the tags
            json_payload['argusMetric']['tags']['Location'] = location
            json_payload['tagVariables'][1]['value'] = location
            print(f'pod: {pod}, Location: {location}, Metric: {metric},seriesId: {seriesId}, transactionId: {transactionId}')
            trace_posting()        # Step #5, 6 (5 comment, 6. uncomment
prepare_json()
######################### END ######################

print("This will be your json payload file\n+++++++++++++++++++++++++\n", json_payload)
