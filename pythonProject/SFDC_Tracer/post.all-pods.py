import requests
'''
!!!! Generates and posts metrics for tracer !!!!
This works fine. It is ugly, but works :)
'''

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjcwNjAwODAxLCJuYmYiOjE2NzA2MDA4MDEsImV4cCI6MTY3MDY0NDAwMSwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.JrGWFhsvOtAf3DgSNoPOfaTQb9EkXCGm4wqNDAym7nH1YIybsx1dNgxhTflGcfy6aCBM-D04rhscoxtIGWQpWPv0R7DQzkTI4UsqtKJuLze73m6oNFNCW03by66QHDAaKR5XNDaZX88a7r9WT3JuYoqmiJZFd5sRgPrWiUAdONPjjfpILKj7ZDBWYqfKvuMpZ2vEM8GsswRpoip1xMqEU4uQIqR3zGuan81vgP4n05Ng6b4mQLb6KSh2IdL-drx1nj9c2XuNUxKMBdYpm55wSL_1h9kh5KHaebOyvxuAMlSnrIM6us6-XWi1L15uwUESKFVTewf_acYn0jzIdxnqfw"}

# Step #0 - Scan through and update few more entries
transactionId=1445340  # This is updated based on the query - https://monitoring.internal.salesforce.com/argusmvp/#/querymanagement

# Step #1
#pod_list=["cs1","cs100","cs101","cs102","cs105","cs106","cs107","cs108","cs109","cs110","cs111","cs112","cs113","cs114","cs115","cs116","cs117","cs119","cs121","cs122","cs123","cs124","cs125","cs126","cs127","cs128","cs129","cs137","cs138","cs14","cs142","cs148","cs15","cs151","cs152","cs159","cs160","cs162","cs165","cs166","cs167","cs169","cs17","cs170","cs171","cs172","cs173","cs174","cs189","cs19","cs190","cs191","cs192","cs193","cs194","cs195","cs196","cs197","cs198","cs199","cs2","cs20","cs200","cs201","cs202","cs203","cs209","cs21","cs210","cs211","cs212","cs213","cs214","cs215","cs216","cs217","cs218","cs219","cs22","cs220","cs221","cs222","cs223","cs224","cs225","cs226","cs23","cs236","cs237","cs238","cs239","cs24","cs240","cs241","cs242","cs243","cs244","cs245","cs246","cs247","cs248","cs249","cs25","cs250","cs251","cs252","cs253","cs258","cs26","cs263","cs264","cs27","cs28","cs29","cs31","cs34","cs35","cs36","cs364","cs365","cs37","cs4","cs40","cs41","cs42","cs43","cs44","cs45","cs46","cs47","cs49","cs5","cs57","cs58","cs59","cs6","cs60","cs61","cs62","cs63","cs67","cs69","cs72","cs73","cs74","cs75","cs76","cs77","cs78","cs79","cs80","cs81","cs84","cs86","cs87","cs88","cs89","cs92","cs94","cs95","cs96","cs97","cs98","cs99"]
#pod_list=["ap0","ap10","ap11","ap12","ap13","ap14","ap15","ap16","ap17","ap18","ap19","ap20","ap21","ap22","ap24","ap25","ap26","ap27","ap28","ap3","ap4","ap5","ap6","ap7","ap8","ap9"]            ## update the list of pods # ## Automate this
#pod_list=["eu16","eu17","eu18","eu19","eu25","eu26","eu27","eu28","eu29","eu30","eu31","eu32","eu33","eu34","eu35","eu36","eu37","eu38","eu39","eu40","eu41","eu42","eu43","eu44","eu45","eu46","eu47","eu48","um1","um2","um3","um4","um5","um6","um7","um8","um9"]
pod_list=["na100","na101","na102","na103","na104","na105","na109","na110","na111","na112","na113","na114","na115","na116","na117","na118","na119","na120","na121","na122","na123","na124","na125","na126","na127","na128","na129","na130","na131","na132","na133","na134","na135","na136","na137","na138","na139","na140","na141","na142","na146","na147","na148","na149","na150","na151","na152","na153","na154","na155","na156","na158","na159","na160","na161","na162","na163","na164","na165","na166","na167","na168","na169","na170","na171","na172","na173","na174","na196","na204","na206","na207","na208","na209","na210","na211","na212","na213","na223","na224","na225","na226","na64","na68","na70","na71","na75","na80","na81","na82","na83","na84","na85","na89","na90","na91","na92","na93","na94","na95","na96","na97","na98","na99"]
#pod_list=["aus1","aus11","aus13","aus23","aus25","aus27","aus3","aus43","aus47","aus5","aus58","aus60","aus62","aus64","aus7","aus75","aus77","aus9","bra1","bra3","bra5","can1","can11","can17","can25","can26","can27","can28","can29","can34","deu1","deu11","deu13","deu25","deu3","deu36","deu38","deu46","deu5","deu52","fra1","fra11","fra19","fra32","fra34","fra36","fra5","fra7","fra9","gbr1","ind1","ind11","ind13","ind15","ind17","ind19","ind21","ind23","ind25","ind27","ind37","ind39","ind41","ind43","ind47","ind5","ind7","ind9","jpn1","jpn17","jpn19","jpn21","jpn3","jpn5","jpn7","kor1","sgp1","sgp10","sgp3","swe1","usa1","usa12","usa13","usa15","usa17","usa19","usa220","usa26","usa34","usa36","usa59","usa61","usa7"]
#pod_list=["aus14s","aus16s","aus18s","aus20s","aus22s","aus24s","aus26s","aus28s","aus2s","aus36s","aus38s","aus4s","aus6s","bra2s","bra4s","bra6s","bra8s","can20s","can2s","can4s","can6s","can8s","deu10s","deu12s","deu14s","deu16s","deu20s","deu2s","deu48s","deu4s","deu50s","deu6s","deu8s","fra12s","fra24s","fra2s","fra4s","fra6s","fra8s","gbr2s","gbr4s","ind10s","ind12s","ind14s","ind16s","ind18s","ind20s","ind22s","ind24s","ind26s","ind28s","ind2s","ind3s","ind4s","ind54s","ind6s","ind8s","jpn10s","jpn12s","jpn18s","jpn20s","jpn22s","jpn24s","jpn28s","jpn2s","jpn4s","jpn6s","jpn8s","kor2s","kor4s","sgp2s","sgp4s","sgp6s","sgp8s","swe2s","swe4s","usa10s","usa16s","usa18s","usa194s","usa196s","usa198s","usa202s","usa20s","usa222s","usa22s","usa24s","usa28s","usa2s","usa30s","usa32s","usa3s","usa60s","usa62s","usa80s","usa8s"]
#pod_list=["cs101"]
#locations_list=["VIR"]
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"] ## Automate this
# Step #3
steps_list=[1,2,3,4,5,6,7,8] ## Automate this
#steps_list=[1] ## Automate this

seriesName = input("Enter seriesName. Valid options are: http_avg, root, db-sql, cache, or soql: ")

metricName = seriesName

if seriesName == "root":
    seriesId = 0
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "http_avg":
    seriesId = 1429719
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
    print()
elif seriesName == "db-sql":
    seriesId = 1429720
    print()
    print(f'You entered:\neriesName:{seriesName}\nseriesId is: {seriesId}\ntransactionId is: {transactionId}')
elif seriesName == "cache":
    seriesId = 1429721
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is:{ transactionId}')
    print()
elif seriesName == "soql":
    seriesId = 1429722
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
                    "id": 2860835,
                    "name": "pod",
                    "value": "ap11"
                },
                {
                    "id": 2860833,
                    "name": "Location",
                    "value": "TYO"
                },
                {
                    "id": 2860834,
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
        print(pod, location, seriesName)
        trace_posting()        # Step #5, 6 (5 comment, 6. uncomment

######################### END ######################

print("This will be your json payload file\n+++++++++++++++++++++++++\n", json_payload)
