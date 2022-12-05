import requests

endpoint = "https://sr-scheduler.internal.salesforce.com/cgi/cuj-auto/replaceables/pods_egl"

r = requests.get(endpoint)

print(r)