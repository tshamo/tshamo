from wipMethods import confirm_prompt
from wipMethods import trace_posting
from wipMethods import setDefaults
from wipMethods import parseJSON
from wipMethods import print_payload
from wipMethods import print_msg

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjcwNTIwNzEyLCJuYmYiOjE2NzA1MjA3MTIsImV4cCI6MTY3MDU2MzkxMiwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.RLrFsyY0GxaaSbRx6qLucWGONgxDRsOL8_70CKy_I81y8hyZhd0rSmQL_fx_wAtCGxvFecCjumMj8hkWkFkKbJwoHhTZMVqT4dUdoaHu4Bq4TOj2s-N3u45Ix2KZpeDH8dW2ElmJaTVaTFFZrDvdN3Qenp-J9DnKsyj_t-nso-8JFBOXBW4CHdqjahCbt1n3x0v2WszC3B02nsMFDEtbG_mQ4aEJk_sRe7lgjauvMIpToevTG0_ea07rVeHtpG4Y-DNojQPGExvnpdkuSTWYDfYVMeCGXUHUS0tMxAVEE87r1BEQ2iYJg0BxOFcu6Uzu7VnM_rJjW80LDoKm5D-2Kg"}

transactionId=1445340
pod_list=["ap0","ap10","ap11","ap12","ap13","ap14","ap15","ap16","ap17","ap18","ap19","ap20","ap21","ap22","ap24","ap25","ap26","ap27","ap28","ap3","ap4","ap5","ap6","ap7","ap8","ap9"]            ## update the list of pods # ## Automate this
locations_list=["VIR","ORE","FRA","DUB","SYD","TYO"]
steps_list=[1,2,3,4,5,6,7,8]

available_metrics = ["http_avg", "db-sql", "cache", "soql"]

mlist=[]

input_string = input(f"Enter seriesName. Valid options are {available_metrics}: ")
input_list = input_string.split()
print(input_list)

## Final confirmation
reply = confirm_prompt("Do you want to proceed?")

for metric in input_list:
    metricName = metric
    seriesName = metric
    seriesId = setDefaults(seriesName,transactionId)
    json_payload = parseJSON(seriesId, seriesName, metricName, transactionId)
    print(json_payload)
    argusMetric = json_payload['argusMetric']

    for pod in pod_list:
        json_payload['argusMetric']['tags']['pod']=pod
        json_payload['tagVariables'][0]['value']=pod

        for location in locations_list:
            json_payload['argusMetric']['tags']['Location'] = location
            json_payload['tagVariables'][1]['value'] = location
            print(pod, location, metricName)
            #print_payload(json_payload)
            trace_posting(transactionId, headers, json_payload)

########################################### END ########################################

#print("This will be your json payload file\n+++++++++++++++++++++++++\n", json_payload)