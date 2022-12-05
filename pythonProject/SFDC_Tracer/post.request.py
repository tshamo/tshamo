import requests

json_payload = {
    "seriesId": 0,
    "seriesName": "root",
    "metricType": "avg",
    "frequencyMin": 10,
    "lookbackMin": 10,
    "delayMin": 10,
    "argusMetric": {
        "metricName": "root",
        "service": "tracer",
        "subService": "",
        "dataCenter": "PRD",
        "superPod": "NONE",
        "pod": "none",
        "tags": {
            "pod": "eu16",
            "seriesName": "root",
            "step": "1",
            "testId": "43901",
            "transactionId": "1409390",
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
            "value": "eu16"
        }
    ]
}

transactionId=1409390

headers = {"Authorization": "eyJ2ZXJzaW9uIjoiMC4xMS4xIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJtb25leC5hcmd1cy5tb25pdG9yaW5nLmF3cy1lc3ZjMS11c2Vhc3QyLmF3cy5zZmRjLmNsIiwiaWF0IjoxNjY5MTM4OTgzLCJuYmYiOjE2NjkxMzg5ODMsImV4cCI6MTY2OTE4MjE4MywiYXVkIjoiTW9uQ2xvdWQiLCJzdWIiOiJ0YXVsYW50LnNoYW1vIiwiZW1haWwiOiJ0YXVsYW50LnNoYW1vQHNhbGVzZm9yY2UuY29tIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidGF1bGFudC5zaGFtbyIsInR5cGUiOiJBQ0NFU1MiLCJ1c2VyZ3JvdXAiOiJbe1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzMjY2YmRkNS1jNWZhLTRjOWYtOTIzZS0yZjdlMmE3NTcwMzVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI2ODIyNzE0Mi00YWRlLTRiYTEtYmJhNS03ZGQ3ZDg0MmEzYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI1NGRmMjBiZS1mMjExLTQ3ODYtYjI5YS01N2Y0Y2VkYjA4YjdcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI4ZmM2OGU2NS00ZTU4LTRmOTgtODBhZS0wMTQxMTJlZGZhOWVcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIzOTlhNzkwNy04OWM1LTRkZTQtYmMxMy01MjcwYjFkN2RlNGFcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI3MzRhNmM4Ny0yN2E3LTQzZjItODdhYy00N2Y4NGMxZWFkYTJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCI5OThhMjcxYS0yZmZkLTQzOGEtYTc2MC02NTg4ZmViNTI5NTZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyMDljNmI5Mi1lZjQxLTQ5ZDgtYmJkNi0yNDZjNjJiZDRiN2ZcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIyNjRmYjI4Yi01YjcyLTQ5MzItOTI2My04YmJjMThmYWFkZDJcIn0se1widXNlckRlZmF1bHRHcm91cEd1aWRcIjpcIlwiLFwiZ3JvdXBHdWlkXCI6XCIwNDgyOTY0ZC01OTU1LTQ2Y2MtYmZjOC1iNGZjMWI1OTQ0NWZcIn1dIn0.sKtULHv5jaTl5henE7C3dzkbH21edszIk5Yuqstby9thNHvWdvO4BXJ7hGTHBxphhv0Fvuaa3WP9IerTNUZsjaDQbu4esTzztjNSflssjuUe5ijzxcMiTwWRt6PrffFp7Zs5OS8HLzxXYU4JM5qlZiqvre_egB9Qb5Roz7elrb359uliFC64HoUM6QZ6r9CGSukS6aMJ4wCM5zT76SHvU2A51KdustWmUG3qURlnORvsuDBLnkBaX0_5wI3wdfRIk7QG5X4BLr_LzIsqQDqD3QRZEidUAkSRWbjED4m-FMi95sxBFSZJkSAJMvEIyHFeLPjHGKi-OeTV-HX4mLteaw"}

endpoint = f'https://tracer-api.sfproxy.monitoring.aws-esvc1-useast2.aws.sfdc.cl/tracer/api/v1/transactionsquery/{transactionId}/publish-metrics'

r = requests.post(endpoint, headers=headers, json=json_payload)
r_dict = r.json()


print(r.status_code)