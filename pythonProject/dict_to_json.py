import json

#dict = {'publishMetricId': 51552, 'transactionId': 1409390, 'seriesId': 0, 'seriesName': 'root', 'metricType': 'avg', 'frequencyMin': 10, 'lookbackMin': 10, 'delayMin': 10, 'argusMetric': {'metricName': 'root', 'service': 'tracer', 'subService': '', 'dataCenter': 'PRD', 'superPod': 'NONE', 'pod': 'none', 'tags': {'pod': 'eu16', 'seriesName': 'root', 'step': '1', 'testId': '43901', 'transactionId': '1409390', 'Location': 'DUB'}}, 'serviceVariables': [], 'spanVariables': [], 'tagVariables': [{'id': 2805554, 'name': 'step', 'value': '1'}, {'id': 2805551, 'name': 'Location', 'value': 'DUB'}, {'id': 2805552, 'name': 'testId', 'value': '43901'}, {'id': 2805553, 'name': 'pod', 'value': 'eu16'}], 'argusExpression': '-1h:tracer.PRD.NONE.none:tracer_root_avg{pod=eu16,seriesName=root,step=1,testId=43901,transactionId=1409390,Location=DUB}:avg:1m-avg', 'monexVariable': None}

#convert dict to a JSON

with open ('sourcedata_dict.json') as access_dict:
    json_object = json.load(access_dict)
#    read_content = json.load(access_json)
    print(json_object)
    print(type(json_object))

