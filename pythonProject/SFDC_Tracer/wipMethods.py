import requests

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

def print_payload(json_payload):
    print(json_payload)

def trace_posting(transactionId, headers, json_payload):
    print("======POSTING======")
    postpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

    r = requests.post(postpoint, headers=headers, json=json_payload)

    print(r)
    print("==================")
#    print(r.url)
#    print(r.headers)
#    print(r.json)

def printMSG(seriesName, seriesId, transactionId):
    print()
    print(f'You entered:\nseriesName: {seriesName}\nseriesId is: {seriesId}\ntransactionId is:{ transactionId}')
    print()

def setDefaults(seriesName,transactionId):
    if seriesName == "root":
        seriesId = 0
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "http_avg":
        seriesId = 1429719
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "db-sql":
        seriesId = 1429720
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "cache":
        seriesId = 1429721
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "soql":
        seriesId = 1429722
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    else:
        print("You entered a wrong option. Exiting ...")
        exit()


def print_msg(json_payload):
    print(json_payload)
    print("+++++++++++++++++++++++++")


def parseJSON(seriesId, seriesName, metricName, transactionId):
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
                "id": 2866917,
                "name": "step",
                "value": "1"
            },
            {
                "id": 2866914,
                "name": "Location",
                "value": "VIR"
            },
            {
                "id": 2866915,
                "name": "testId",
                "value": "43901"
            },
            {
                "id": 2866916,
                "name": "pod",
                "value": "usa1"
            }
        ],
        "argusExpression": "-1h:tracer.PRD.NONE.none:tracer_http_resp_avg{pod=ap11,seriesName=http_resp,testId=43901,transactionId=1435693,Location=TYO}:avg:1m-avg",
        "monexVariable": "test"
    }

    del json_payload['argusExpression']
    del json_payload['monexVariable']

    print("This will be your json payload file\n----------------------------------------")

    return json_payload

## WIP ##
def generatePayload(pod_list, metricName, locations_list, json_payload, input_list, transactionId):
    for metric in input_list:
        metricName = metric
        seriesName = metric
        seriesId = setDefaults(seriesName, transactionId)
        json_payload = parseJSON(seriesId, seriesName, metricName, transactionId)
        print(json_payload)
        argusMetric = json_payload['argusMetric']

        for pod in pod_list:
            json_payload['argusMetric']['tags']['pod']=pod
            json_payload['tagVariables'][3]['value']=pod
            #print(pod)
            for location in locations_list:
                json_payload['argusMetric']['tags']['Location'] = location
                json_payload['tagVariables'][1]['value'] = location
                print(pod, location, metricName)

                for step in locations_list:
                    json_payload['argusMetric']['tags']['Location'] = location
                    json_payload['tagVariables'][1]['value'] = location
                    print(pod, location, metricName)

                return pod, location, metricName
            #trace_posting(transactionId, headers, json_payload)