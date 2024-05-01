import csv

filename = 'students.csv'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        #print(row) ['Ruslan', '23B202424', '1', '+77007007070']
                    #['Mariya', '23B202425', '1', '+77077077070']
        name, id, study_year, phone_number = row
        # print(name, id, study_year, phone_number) Ruslan 23B202424 1 +77007007070 
                                                    #Mariya 23B202425 1 +77077077070
