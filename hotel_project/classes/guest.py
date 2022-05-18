class Guest:
    guests = []

    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.guests.append(self)
