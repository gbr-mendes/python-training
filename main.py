import sys

from classes.errors import CpfValidationError
from classes.room import Room
from classes.system import System
from constants import HOTEL_NAME, OPTIONS


def system_loop():
        quit_option = list(OPTIONS.values()).index('Quit') + 1
        check_in_options = list(OPTIONS.values()).index('Check-in guest') + 1
        check_out_options = list(OPTIONS.values()).index('Check-out guest') + 1

        options = list(OPTIONS.keys())
        option = int(System.input_option())

        while option != quit_option:
            if not str(option) in options:
                print('Please, type a valid option!')
                System.display_options(OPTIONS)
                option = int(System.input_option())
            else:
                if option == check_in_options:
                    System.check_in()
                elif option == check_out_options:
                    System.check_out()
                
            main(load_rooms=False)

def main(load_rooms=True):
    if load_rooms:
        Room.load_rooms()
    
    System.hotel_greetings(HOTEL_NAME)
    System.display_options(OPTIONS)

    try:
        system_loop()
    except CpfValidationError:
        print('CPF invalid. Try again!')
        main(load_rooms=False)
    except ValueError:
        print('An error has ocurred in the data input. Try again')
        System.display_options(OPTIONS)
        system_loop()
    except Exception as e:
        raise e
        print('Unexpected error')
        sys.exit()


if __name__ == '__main__':
    main()
