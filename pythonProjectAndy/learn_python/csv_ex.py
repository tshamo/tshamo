import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # We don't what the first 2 lines. skipping 2 lines
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward': ## dont't list the names below 'No Reward'
            break
        names.append(f"{line[0]} {line[1]}") # index 0 firstname and 1 lastname

for name in names:
    print(name)

html_output += f'<p>There are currently {len(names)} public contributers. Thank you!</p>'
html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output +='\n</u>'

print(html_output)