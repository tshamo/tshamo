import requests
'''
!!!! Generates and posts metrics for tracer !!!!
This works fine. It is ugly, buy works :)
'''

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5MTM4OTgzLCJuYmYiOjE2NjkxMzg5ODMsImV4cCI6MTY2OTE4MjE4MywiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.sKtULHv5jaTl5henE7C3dzkbH21edszIk5Yuqstby9thNHvWdvO4BXJ7hGTHBxphhv0Fvuaa3WP9IerTNUZsjaDQbu4esTzztjNSflssjuUe5ijzxcMiTwWRt6PrffFp7Zs5OS8HLzxXYU4JM5qlZiqvre_egB9Qb5Roz7elrb359uliFC64HoUM6QZ6r9CGSukS6aMJ4wCM5zT76SHvU2A51KdustWmUG3qURlnORvsuDBLnkBaX0_5wI3wdfRIk7QG5X4BLr_LzIsqQDqD3QRZEidUAkSRWbjED4m-FMi95sxBFSZJkSAJMvEIyHFeLPjHGKi-OeTV-HX4mLteaw"}

# Step #0 - Scan through and update few more entries
transactionId=1421118  # This is updated based on the query - https://monitoring.internal.salesforce.com/argusmvp/#/querymanagement

# Step #1
pod_list=["na100","na101","na102","na103","na104","na105","na109","na110","na111","na112","na113","na114","na115","na116","na117","na118","na119","na120","na121","na122","na123","na124","na125","na126","na127","na128","na129","na130","na131","na132","na133","na134","na135","na136","na137","na138","na139","na140","na141","na142","na146","na147","na148","na149","na150","na151","na152","na153","na154","na155","na156","na158","na159","na160","na161","na162","na163","na164","na165","na166","na167","na168","na169","na170","na171","na172","na173","na174","na196","na204","na206","na207","na208","na209","na210","na211","na212","na213","na223","na224","na225","na226","na64","na68","na70","na71","na75","na80","na81","na82","na83","na84","na85","na89","na90","na91","na92","na93","na94","na95","na96","na97","na98","na99"]            ## update the list of pods # ## Automate this
# Step #2
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"] ## Automate this
# Step #3
steps_list=[1,2,3,4,5,6,7,8] ## Automate this

json_payload = {
    "seriesId": 1402075,          # Step #0
    "seriesName": "http_resp_time",   # Step #0
    "metricType": "avg",
    "frequencyMin": 10,
    "lookbackMin": 10,
    "delayMin": 10,
    "argusMetric": {
        "metricName": "http_resp_time",   # Step #0
        "service": "tracer",
        "subService": "",
        "dataCenter": "PRD",
        "superPod": "NONE",
        "pod": "none",
        "tags": {
            "pod": "fra19",
            "seriesName": "http_resp_time",   # Step #0
            "step": "1",
            "testId": "43901",
            "transactionId": "1421118",
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

argusMetric = json_payload['argusMetric'] ## get argusMetric
tags = argusMetric['tags']          ## get tags within argusMetric
step = tags['step']                 ## get step within tags that is in argusMetric

tagVariables = json_payload['tagVariables']
tag_step = tagVariables[0]['value']

message = f'argusMetric: {argusMetric}\n\ntags: {tags}\n\nstep: {step}\n\ntagVariables:{tagVariables}\n\n'
tag_step_msg = f'tag_step: {tag_step}'
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