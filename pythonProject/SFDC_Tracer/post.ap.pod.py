import requests
'''
!!!! Generates and posts metrics for tracer !!!!
This works fine. It is ugly, buy works :)
'''

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5OTA2MTkyLCJuYmYiOjE2Njk5MDYxOTIsImV4cCI6MTY2OTk0OTM5MiwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.hAW8r8PTY76xlxRXJB_GilZaq2uTjsTYt7CmsJR_IIkFEQmorBPXod4wIilb1Fs6t88wfuR7ALGAnY-y70H8lP0PLJJYq5lPVj685rwMPNcG9nCc1gHsqK0dRrdXj8DOKA5nPSq_nnHwVHWGSCJPlhytr7yLNxjIOupG8mmKaaOkMrNO9sYhTjWAXXcsQ4xw40tj7ivteg-tMCJY6zARfgHp8oAfsmT8ULd_nYzO1NNz7prWD3NtsuzBs2Hsm09MfzTb2ufOH4dkUInx6jpZwL8g_y7sEuRTkqF0stcmRFC5JwCGPdA_iqLzpKke8TwtMSUuxyabLd9iJU0msWg5Qg"}

# Step #0 - Scan through and update few more entries
transactionId=1435693  # This is updated based on the query - https://monitoring.internal.salesforce.com/argusmvp/#/querymanagement

# Step #1
#pod_list=["ap0","ap10","ap11","ap12","ap13","ap14","ap15","ap16","ap17","ap18","ap19","ap20","ap21","ap22","ap24","ap25","ap26","ap27","ap28","ap3","ap4","ap5","ap6","ap7","ap8","ap9"]            ## update the list of pods # ## Automate this
pod_list=["ap0","ap20","ap21","ap22","ap24","ap25","ap26","ap27","ap28","ap3","ap4","ap5","ap6","ap7","ap8","ap9"]            ## update the list of pods # ## Automate this

# Step #2
#locations_list=["VIR"]
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"] ## Automate this
# Step #3
steps_list=[1,2,3,4,5,6,7,8] ## Automate this
#steps_list=[1] ## Automate this

seriesName = input("Enter seriesName. Valid options are: http_resp, root, db-sql, cache, or soql: ")

metricName = seriesName

if seriesName == "root":
    seriesId = 0
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "http_resp":
    seriesId = 1422299
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "db-sql":
    seriesId = 1422300
    print()
    print(f'You entered:\neriesName:{seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
elif seriesName == "cache":
    seriesId = 1422301
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is:{ transactionId}')
    print()
elif seriesName == "soql":
    seriesId = 1422302
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is:{ transactionId}')
    print()
else:
    print("You entered a wrong option. Exiting ...")
    exit()

json_payload =         {
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

del json_payload['argusExpression']
del json_payload['monexVariable']

argusMetric = json_payload['argusMetric'] ## get argusMetric               ## get step within tags that is in argusMetric

######################### LAST CONFIRMATION ##################

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


########### POSTING #####
def trace_posting():
    print("===============POSTING====================")
    postpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

    r = requests.post(postpoint, headers=headers, json=json_payload)

    print(r)
#########################

def print_msg():
    print(json_payload)
    print("+++++++++++++++++++++++++")
#########################
for pod in pod_list:
    json_payload['argusMetric']['tags']['pod']=pod   ## updated the step
    json_payload['tagVariables'][0]['value']=pod
    #print(pod)
    for location in locations_list:  ## updated the step under the tags
        json_payload['argusMetric']['tags']['Location'] = location
        json_payload['tagVariables'][1]['value'] = location
        print(pod, location)
        trace_posting()        # Step #5, 6 (5 comment, 6. uncomment

######################### END ######################

print("This will be your json payload file\n+++++++++++++++++++++++++\n", json_payload)
