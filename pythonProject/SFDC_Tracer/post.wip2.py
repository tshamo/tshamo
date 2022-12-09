from wipMethods import confirm_prompt
from wipMethods import trace_posting
from wipMethods import setDefaults
from wipMethods import parseJSON
from wipMethods import print_payload
from wipMethods import print_msg

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjcwNTIwNzEyLCJuYmYiOjE2NzA1MjA3MTIsImV4cCI6MTY3MDU2MzkxMiwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.RLrFsyY0GxaaSbRx6qLucWGONgxDRsOL8_70CKy_I81y8hyZhd0rSmQL_fx_wAtCGxvFecCjumMj8hkWkFkKbJwoHhTZMVqT4dUdoaHu4Bq4TOj2s-N3u45Ix2KZpeDH8dW2ElmJaTVaTFFZrDvdN3Qenp-J9DnKsyj_t-nso-8JFBOXBW4CHdqjahCbt1n3x0v2WszC3B02nsMFDEtbG_mQ4aEJk_sRe7lgjauvMIpToevTG0_ea07rVeHtpG4Y-DNojQPGExvnpdkuSTWYDfYVMeCGXUHUS0tMxAVEE87r1BEQ2iYJg0BxOFcu6Uzu7VnM_rJjW80LDoKm5D-2Kg"}

transactionId=1445340
#pod_list=["cs1","cs100","cs101","cs102","cs105","cs106","cs107","cs108","cs109","cs110","cs111","cs112","cs113","cs114","cs115","cs116","cs117","cs119","cs121","cs122","cs123","cs124","cs125","cs126","cs127","cs128","cs129","cs137","cs138","cs14","cs142","cs148","cs15","cs151","cs152","cs159","cs160","cs162","cs165","cs166","cs167","cs169","cs17","cs170","cs171","cs172","cs173","cs174","cs189","cs19","cs190","cs191","cs192","cs193","cs194","cs195","cs196","cs197","cs198","cs199","cs2","cs20","cs200","cs201","cs202","cs203","cs209","cs21","cs210","cs211","cs212","cs213","cs214","cs215","cs216","cs217","cs218","cs219","cs22","cs220","cs221","cs222","cs223","cs224","cs225","cs226","cs23","cs236","cs237","cs238","cs239","cs24","cs240","cs241","cs242","cs243","cs244","cs245","cs246","cs247","cs248","cs249","cs25","cs250","cs251","cs252","cs253","cs258","cs26","cs263","cs264","cs27","cs28","cs29","cs31","cs34","cs35","cs36","cs364","cs365","cs37","cs4","cs40","cs41","cs42","cs43","cs44","cs45","cs46","cs47","cs49","cs5","cs57","cs58","cs59","cs6","cs60","cs61","cs62","cs63","cs67","cs69","cs72","cs73","cs74","cs75","cs76","cs77","cs78","cs79","cs80","cs81","cs84","cs86","cs87","cs88","cs89","cs92","cs94","cs95","cs96","cs97","cs98","cs99"]
pod_list=["na100","na101","na102","na103","na104","na105","na109","na110","na111","na112","na113","na114","na115","na116","na117","na118","na119","na120","na121","na122","na123","na124","na125","na126","na127","na128","na129","na130","na131","na132","na133","na134","na135","na136","na137","na138","na139","na140","na141","na142","na146","na147","na148","na149","na150","na151","na152","na153","na154","na155","na156","na158","na159","na160","na161","na162","na163","na164","na165","na166","na167","na168","na169","na170","na171","na172","na173","na174","na196","na204","na206","na207","na208","na209","na210","na211","na212","na213","na223","na224","na225","na226","na64","na68","na70","na71","na75","na80","na81","na82","na83","na84","na85","na89","na90","na91","na92","na93","na94","na95","na96","na97","na98","na99"]
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