import json

myDict = {'a':['apple', 'avacado'], 'b':['banana', 'berry'], 'vitamins':2.0142}
jsonStr = json.dumps(myDict)

print(jsonStr)