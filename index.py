import csv

print('bus app')

def buyTickets():
    with open('mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile: