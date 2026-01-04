print('bus app')


# Menu system

while True:
    try:
        menuInput = int(input('Wellcome to Bus Ticket App\n1. To buy tickets enter 1\n2. To log in as an admin press 2\n0. To exit enter 0\n>>>'))

        # Alternative to if
        match menuInput:
            case 1:
                print('buy tickets')
            case 2:
                print('admin')
            case 0:
                exit()
            case _:
                print('Please enter a correct number. Valid numbers are 1, 2 and 0\n')

    # Expecting a user to enter a letter
    except ValueError:
        print('Please enter a valid input. A valid input is a number\n')
