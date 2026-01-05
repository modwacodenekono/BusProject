import csv

print('bus app')

categoryList = []

def buyTickets():
    with open('mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines['category_title'] not in categoryList:
                categoryList.append(lines['category_title'])


buyTickets()
for data in categoryList:
    print(data)
inp = True
#error handling
while inp:
    categoryChoice = int(input('What would you like to buy?\n>>>'))
    if 0 <= categoryChoice - 1 <= len(categoryList):
        inp = False
        print('You have chosen ' + categoryList[categoryChoice - 1])
    else:
        print('Invalid choice')