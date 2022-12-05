
valid_metric_list = ["root","http_resp","cache","db-sql","soql"]

def valid_metric_check(prompt):
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print("Sorry, that is not a valid metric.")
            continue

        if value not in valid_metric_list:
            print("Sorry, that is not a valid metric. Valid list is", valid_metric_list)
            continue
        else:
            break
    return value

metric = valid_metric_check("Enter metric: ")


metrics_var = {'root':{"seriesId": 0},'http_resp':{"seriesId": 1422556},'db-sql':{"seriesId": 1422557},'cache':{"seriesId": 1422558},'soql':{"seriesId": 1422559} }

def set_metric_defaults(*args):
    for arg in args:
        seriesName = arg
        for k, j in metrics_var[arg].items():
            seriesId = j
            seriesName = arg
            print(seriesName, seriesId)
    return seriesName, seriesId

set_metric_defaults(metric)


