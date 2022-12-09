import requests

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjcwNjAxNDAwLCJuYmYiOjE2NzA2MDE0MDAsImV4cCI6MTY3MDY0NDYwMCwiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.R6kQNKJ8t2idwAH6w9z67Uunp_zZn4aE2ds6fPBnJsR_R99OsK58i540ORMlOLw6R5uM5Sk8_dQ8SVTEov09OFzdDWV5-6WQv6u9SRqDQsIyS9AzexzcXyzHtSb6_LQ7jFEC7-dnVIUxkqPRsdPQc-sRyYfGT5ceHswKyo2Ieyiiq4Wu6rvBg7sCIO82tcyN9ZWBWOycciayvsJExKe5sC9We88Q_faZ8FN3nd5kpR-6tV2YasbKxOpoEBg8J-Jnea1TY-gTcnrek5167Bd2S_SXeyhlrlb0flcECGwRsZMtUQgJuHzXn6vfUQoo0oIutAyCOMEPGHrlj6LJDmgxiw"}

transactionId=1445340

endpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

r = requests.get(endpoint, headers=headers)
r_dict = r.json()

publishMetrics = r_dict["publishMetrics"]

count=0
for i in publishMetrics:

    seriesId = i["seriesId"]
    publishMetricId = i["publishMetricId"]
    seriesName = i["seriesName"]
    argusMetric = i["argusMetric"]
    tags = argusMetric["tags"]
    pod = tags["pod"]
    #step = tags["step"]
    #if "step" in tags and seriesName == "db-sql":
    if pod == "ap9":
        count += 1
        print(count)
        #print(f'publishMetricId: {publishMetricId}, seriesId: {seriesId}, seriesName: {seriesName}, pod: {pod}, step: {step}')
        print(f'tags: {tags}, publishMetricId: {publishMetricId}, seriesId: {seriesId}')
        #delendpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics/{publishMetricId}'
        #r = requests.delete(delendpoint, headers=headers)
        #print(r.status_code, publishMetricId, "deleted")

    else:
        continue