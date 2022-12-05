import requests
'''
!!!! Generates and posts metrics for tracer !!!!
This works fine. It is ugly, buy works :)
'''

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5OTA2MTkyLCJuYmYiOjE2Njk5MDYxOTIsImV4cCI6MTY2OTk0OTM5MiwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.hAW8r8PTY76xlxRXJB_GilZaq2uTjsTYt7CmsJR_IIkFEQmorBPXod4wIilb1Fs6t88wfuR7ALGAnY-y70H8lP0PLJJYq5lPVj685rwMPNcG9nCc1gHsqK0dRrdXj8DOKA5nPSq_nnHwVHWGSCJPlhytr7yLNxjIOupG8mmKaaOkMrNO9sYhTjWAXXcsQ4xw40tj7ivteg-tMCJY6zARfgHp8oAfsmT8ULd_nYzO1NNz7prWD3NtsuzBs2Hsm09MfzTb2ufOH4dkUInx6jpZwL8g_y7sEuRTkqF0stcmRFC5JwCGPdA_iqLzpKke8TwtMSUuxyabLd9iJU0msWg5Qg"}

# Step #0 - Scan through and update few more entries
transactionId=1421118  # This is updated based on the query - https://monitoring.internal.salesforce.com/argusmvp/#/querymanagement

# Step #1
#pod_list=["na173","na174"]
#pod_list=["eu15","eu16""eu17","eu18","eu19"]            ## update the list of pods # ## Automate this
#pod_list=[cs1,cs100,cs101,cs102,cs105,cs106,cs107,cs108,cs109,cs110,cs111,cs112,cs113,cs114,cs115,cs116,cs117,cs119,cs121,cs122,cs123,cs124,cs125,cs126,cs127,cs128,cs129,cs137,cs138,cs14,cs142,cs148,cs15,cs151,cs152,cs159,cs160,cs162,cs165,cs166,cs167,cs169,cs17,cs170,cs171,cs172,cs173,cs174,cs189,cs19,cs190,cs191,cs192,cs193,cs194,cs195,cs196,cs197,cs198,cs199,cs2,cs20,cs200,cs201,cs202,cs203,cs209,cs21,cs210,cs211,cs212,cs213,cs214,cs215,cs216,cs217,cs218,cs219,cs22,cs220,cs221,cs222,cs223,cs224,cs225,cs226,cs23,cs236,cs237,cs238,cs239,cs24,cs240,cs241,cs242,cs243,cs244,cs245,cs246,cs247,cs248,cs249,cs25,cs250,cs251,cs252,cs253,cs258,cs26,cs263,cs264,cs27,cs28,cs29,cs31,cs34,cs35,cs36,cs364,cs365,cs37,cs4,cs40,cs41,cs42,cs43,cs44,cs45,cs46,cs47,cs49,cs5,cs57,cs58,cs59,cs6,cs60,cs61,cs62,cs63,cs67,cs69,cs72,cs73,cs74,cs75,cs76,cs77,cs78,cs79,cs80,cs81,cs84,cs86,cs87,cs88,cs89,cs92,cs94,cs95,cs96,cs97,cs98,cs99,%  taulant.shamo@taulantsha-wsm ~ % for pod in `cat cs.list`; do echo -n \"$pod\",; done
pod_list="cs1","cs100","cs101","cs102","cs105","cs106","cs107","cs108","cs109","cs110","cs111","cs112","cs113","cs114","cs115","cs116","cs117","cs119","cs121","cs122","cs123","cs124","cs125","cs126","cs127","cs128","cs129","cs137","cs138","cs14","cs142","cs148","cs15","cs151","cs152","cs159","cs160","cs162","cs165","cs166","cs167","cs169","cs17","cs170","cs171","cs172","cs173","cs174","cs189","cs19","cs190","cs191","cs192","cs193","cs194","cs195","cs196","cs197","cs198","cs199","cs2","cs20","cs200","cs201","cs202","cs203","cs209","cs21","cs210","cs211","cs212","cs213","cs214","cs215","cs216","cs217","cs218","cs219","cs22","cs220","cs221","cs222","cs223","cs224","cs225","cs226","cs23","cs236","cs237","cs238","cs239","cs24","cs240","cs241","cs242","cs243","cs244","cs245","cs246","cs247","cs248","cs249","cs25","cs250","cs251","cs252","cs253","cs258","cs26","cs263","cs264","cs27","cs28","cs29","cs31","cs34","cs35","cs36","cs364","cs365","cs37","cs4","cs40","cs41","cs42","cs43","cs44","cs45","cs46","cs47","cs49","cs5","cs57","cs58","cs59","cs6","cs60","cs61","cs62","cs63","cs67","cs69","cs72","cs73","cs74","cs75","cs76","cs77","cs78","cs79","cs80","cs81","cs84","cs86","cs87","cs88","cs89","cs92","cs94","cs95","cs96","cs97","cs98","cs99"]            ## update the list of pods # ## Automate this
# Step #2
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"] ## Automate this
# Step #3
steps_list=[1,2,3,4,5,6,7,8] ## Automate this

seriesName = input("Enter seriesName. Valid options are: http_app, root, db-sql, cache, or soql: ")

if seriesName == "root":
    seriesId = 0
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "http_app":
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
