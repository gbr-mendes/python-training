from .errors import  CpfValidationError
from .room import Room
from .guest import Guest
from validate_docbr import CPF

from utils import helpers


class System:

    @staticmethod
    def hotel_greetings(hotel_name):
        # Mensagem inicial do sistema
        helpers.separator()
        helpers.print_center(f'Welcome to the {hotel_name}')
        helpers.separator()

    @staticmethod
    def display_options(options):
        # Exibe as opções disponíveis no sistema
        for key, value in options.items():
            print(f'{key} - {value}')
        helpers.separator()

    @staticmethod
    # Entrada de dados para seleção de opção no sistema
    def input_option():
        option = input('Type your option: ')
        return option

    @classmethod
    def select_room(cls):
        room_id = input('Select a room: ')
        for room in Room.rooms:
            if str(room.id) == room_id:
                if room.available:
                    room.set_as_unavailable()
                    return room
        print('Please, select an available room!')
        cls.select_room()

    @classmethod
    def find_guest(cls):
        guest_cpf = input('Type the guest CPF:')
        for guest in Guest.guests:
            if guest.cpf == guest_cpf:
                return guest
        print('Guest not found. Try again!')
        return cls.find_guest()

    @staticmethod
    # check-in de guest
    def check_in():
        helpers.separator()
        helpers.print_center('CHECK-IN')
        name = input('Please, type your name: ')

        # Valida o cpf para depois instanciar um Guest
        cpf_validator = CPF()
        cpf = input('Please, type your CPF: ')
        if not cpf_validator.validate(cpf):
            raise CpfValidationError
        
        # instancia de Guest
        guest = Guest(name, cpf)
        
        # Exibe os quartos disponíveis
        Room.show_rooms()

        # Armazena quarto selecionado
        room = System.select_room()

        # Atribui quarto selecionado ao guest
        guest.room = room
        
        print(f'Check-in successfully. Welcome {guest.name}')
        helpers.separator()
    
    @staticmethod
    def check_out():
        if len(Guest.guests) > 0:
            helpers.print_center('CHECK-OUT')
            guest = System.find_guest()

            confirmation = input(f'Are you sure that you wanna check-out {guest.name}?(y/n)')
            if confirmation == 'y':
                guest.room.set_as_available()
                Guest.guests.remove(guest)
                print('Guest checked-out successfully')
        else:
            print('No guests to check-out')
        

