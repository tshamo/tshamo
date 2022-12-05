import requests
'''
!!!! Generates and posts metrics for tracer !!!!
This works fine. It is ugly, buy works :)
'''

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5MzA4NjA1LCJuYmYiOjE2NjkzMDg2MDUsImV4cCI6MTY2OTM1MTgwNSwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.dd9Xv_LHVC6GvmCb0Nl6SLglCa1zAoKNHE_3xXGm2E4n4PUIT3o50EWpTmYypW-0gWfY_XA1cfKyzaDGLcHZJ8tu7erYiiUTI71dWCklxkY7IkT0vhIsJceTC_Gs1Q8Lz2CQaVtwRxcUufTguBVFTc-gJ2LRlOJUeiHuNHpnC6ysg8Y4WRFu5GhGTGdpZqRya1P-LNhDj5mmxdRV7VrKx9tWq2uBbtjRZIMqqP5WOIGbYe9aVqUYXse6QulsfZkakvP4Jo952lGBmTdCQWnkV3a9GwjmB006GvhYxBTjDEMXH_zBK5qivWrTpCaRDA_Bga1gkmifkgSugG-SqJgzZA"}

# Step #0 - Scan through and update few more entries
transactionId=1421118  # This is updated based on the query - https://monitoring.internal.salesforce.com/argusmvp/#/querymanagement

# Step #1
#pod_list=["na173","na174"]
pod_list=["eu15","eu16""eu17","eu18","eu19"]            ## update the list of pods # ## Automate this
#pod_list=["na173","na174","na196","na204","na206","na207","na208","na209","na210","na211","na212","na213","na223","na224","na225","na226","na64","na68","na70","na71","na75","na80","na81","na82","na83","na84","na85","na89","na90","na91","na92","na93","na94","na95","na96","na97","na98","na99"]            ## update the list of pods # ## Automate this
# Step #2
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"] ## Automate this
# Step #3
steps_list=[1,2,3,4,5,6,7,8] ## Automate this

seriesName = input("Enter seriesName. Valid options are: apt, root, db-sql, cache, or soql: ")

if seriesName == "root":
    seriesId = 0
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "apt":
    seriesId =  1402075
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "db-sql":
    seriesId = 1402076
    print()
    print(f'You entered:\neriesName:{seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
elif seriesName == "cache":
    seriesId = 1402077
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is:{ transactionId}')
    print()
else:
    print("You entered a wrong option. Exiting ...")
    exit()


json_payload = {
    "seriesId": seriesId,
    "seriesName": seriesName,
    "metricType": "avg",
    "frequencyMin": 10,
    "lookbackMin": 10,
    "delayMin": 10,
    "argusMetric": {
        "metricName": seriesName,
        "service": "tracer",
        "subService": "",
        "dataCenter": "PRD",
        "superPod": "NONE",
        "pod": "none",
        "tags": {
            "pod": "fra19",
            "seriesName": seriesName,
            "step": "1",
            "testId": "43901",
            "transactionId": transactionId,
            "Location": "VIR"
        }
    },
    "serviceVariables": [],
    "spanVariables": [],
    "tagVariables": [
        {
            "id": 2805554,
            "name": "step",
            "value": "1"
        },
        {
            "id": 2805551,
            "name": "Location",
            "value": "VIR"
        },
        {
            "id": 2805552,
            "name": "testId",
            "value": "43901"
        },
        {
            "id": 2805553,
            "name": "pod",
            "value": "fra19"
        }
    ]
}
print("This will be your json payload file\n----------------------------------------")
print (json_payload)

argusMetric = json_payload['argusMetric'] ## get argusMetric
tags = argusMetric['tags']          ## get tags within argusMetric
step = tags['step']                 ## get step within tags that is in argusMetric

tagVariables = json_payload['tagVariables']
tag_step = tagVariables[0]['value']

message = f'argusMetric: {argusMetric}\n\ntags: {tags}\n\nstep: {step}\n\ntagVariables:{tagVariables}\n\n'
tag_step_msg = f'tag_step: {tag_step}'
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
    json_payload['tagVariables'][3]['value']=pod
    print(pod)
    for location in locations_list:  ## updated the step under the tags
        json_payload['argusMetric']['tags']['Location'] = location
        json_payload['tagVariables'][1]['value'] = location
        print(location)
        for step in steps_list:
            json_payload['argusMetric']['tags']['step']=step   ## updated the step
            json_payload['tagVariables'][0]['value']=step
            print(pod,location,step)
            print("+++++++++++++++++++++++++")
            print_msg()
            #trace_posting()        # Step #5, 6 (5 comment, 6. uncomment

######################### END ######################

print("This will be your json payload file\n+++++++++++++++++++++++++\n", json_payload)
