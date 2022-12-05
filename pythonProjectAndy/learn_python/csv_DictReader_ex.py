import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # We don't what first line of bad data
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':  ## dont't list the names below 'No Reward'
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

for name in names:
    print(name)

html_output += f'<p>There are currently {len(names)} public contributers. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</u>'

print(html_output)
