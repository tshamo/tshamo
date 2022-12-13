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


def setDefaults(seriesName,transactionId):
    if seriesName == "root":
        seriesId = 0
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "http_avg":
        seriesId = 1432760
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "db-sql":
        seriesId = 1432761
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "cache":
        seriesId = 1432762
        printMSG(seriesName,seriesId,transactionId)
        return seriesId
    elif seriesName == "soql":
        seriesId = 1432763
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
            "seriesName": metricName,
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
                    "pod": "pod",
                    "seriesName": seriesName,
                    "step": "1",
                    "testId": "43901",
                    "transactionId": transactionId,
                    "Location": "VIR"
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
            "argusExpression": "-1h:tracer.PRD.NONE.none:tracer_http_avg_avg{pod=usa1,seriesName=http_avg,step=1,testId=43901,transactionId=1449288,Location=VIR}:avg:1m-avg",
            "monexVariable": "null"
        }


    del json_payload['argusExpression']
    del json_payload['monexVariable']

    print("This will be your json payload file\n----------------------------------------")

    return json_payload
