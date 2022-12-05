import csv

with open('nameS.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)       # comma , by default, otherwise specify

    #next(csv_reader)        # skips the first line
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')    ## new file with - as delimiteror \t tab or ;

        for line in csv_reader:
            csv_writer.writerow(line)