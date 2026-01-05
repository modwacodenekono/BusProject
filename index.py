import csv

print('bus app')

categoryList = []

def buyTickets():
    with open('mobile_products.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            if lines['category_title'] not in categoryList:
                categoryList.append(lines['category_title'])

    chooseCategory()




def chooseCategory():
    i = 1
    terminateLoop = True

    for data in categoryList:
        print(i + '.', data)
        i += 1

    #error handling
    while terminateLoop:
        categoryChoice = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        if 0 <= categoryChoice - 1 <= len(categoryList):
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoice - 1])


        else:
            print('Invalid choice')

def confirmChoice():
    inp2 = input('1. To find out more or\n2. To buy a ticket or\n0. To exit\n>>>')

    while terminateLoop:
        categoryChoice = int(input('To find out more or buy a ticket please enter the number.\n>>>'))
        if 0 <= categoryChoice - 1 <= len(categoryList):
            terminateLoop = False
            print('You have chosen ' + categoryList[categoryChoice - 1])


        else:
            print('Invalid choice')


buyTickets()