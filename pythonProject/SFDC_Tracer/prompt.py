valid_metric_list = ["root","apt","cache","db-sql","soql"]

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