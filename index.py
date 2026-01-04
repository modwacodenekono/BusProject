print('bus app')


# Menu system

menuInput = input('Wellcome to Bus Ticket App\n1. To buy tickets enter 1\n 2. To log in as an admin press 2\n 0. To exit enter 0' )


match menuInput:
    case 1:
        print('buy tickets')
    case 2:
        print('admin')
    case 0:
        exit()
    case _:
