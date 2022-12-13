import requests

def getMetricSeriesIds(json_payload):
    transaction = json_payload["transaction"]
    path = transaction["path"]
    compute = transaction["compute"]

    id_metric_dict = {}

    for j in compute:
        for k in j["metrics"]:
            id_metric_dict[k["name"]] = k["id"]
    return(id_metric_dict)


def getReplaceablesIds(json_payload):
    transaction = json_payload["transaction"]
    path = transaction["path"]
    root = path["root"]
    tags = root["tags"]

    id_replaceables_dict={}

    for i in tags:
        if i["variable"] == "Location":
            variable_Location_id = i["id"]
            id_replaceables_dict["Location"] = variable_Location_id
        elif i["variable"] == "testId":
            variable_testId_id = i["id"]
            id_replaceables_dict["testId"] = variable_testId_id

        elif i["variable"] == "pod":
            variable_pod_id = i["id"]
            id_replaceables_dict["pod"] = variable_pod_id

        else:
            print("Something is not right")

    return id_replaceables_dict


def parseJSON(seriesId, seriesName, metricName, transactionId, pod_id, Location_id, testId_id, testId):
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
                "testId": testId,
                "transactionId": transactionId,
                "Location": "TYO"
            }
        },
        "tagVariables": [
            {
                "id": pod_id,
                "name": "pod",
                "value": "ap11"
            },
            {
                "id": Location_id,
                "name": "Location",
                "value": "TYO"
            },
            {
                "id": testId_id,
                "name": "testId",
                "value": "43901"
            }
        ],
        "argusExpression": "-1h:tracer.PRD.NONE.none:tracer_http_resp_avg{pod=ap11,seriesName=http_resp,testId=43901,transactionId=1435693,Location=TYO}:avg:1m-avg",
        "monexVariable": "test"
    }

    del json_payload['argusExpression']
    del json_payload['monexVariable']

    return json_payload

def post_payload(transactionId, headers, parsed_json):
    print("======POSTING======")
    postpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

    r = requests.post(postpoint, headers=headers, json=parsed_json)

    print(r)
    print("==================")
#    print(r.url)
#    print(r.headers)
#    print(r.json)


'''
def GetFinalPayload(pod_list, parsed_json, locations_list):
    for pod in pod_list:
        parsed_json['argusMetric']['tags']['pod'] = pod
        parsed_json['tagVariables'][0]['value'] = pod

        for location in locations_list:
            parsed_json['argusMetric']['tags']['Location'] = location
            parsed_json['tagVariables'][1]['value'] = location
            print(parsed_json)
    
    return parsed_json

'''

def getKaijuTestId(json_payload):
    transaction = json_payload["transaction"]
    path = transaction["path"]
    root = path["root"]
    tags = root["tags"]

    for i in tags:
        if i["name"] == "sfdc.kaijuTestId":
            kaiju_testId = i["value"]
        else:
            continue

    return kaiju_testId

def validate_input(input_list, available_metrics):
    for i in input_list:
        if i not in available_metrics:
            print("Not a valid metric. Exiting ... Try again.")
            exit()
        else:
           pass

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