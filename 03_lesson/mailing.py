from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track


    def __int__(self):

        return f"отправление {self.track} из {self.address1} в {self.address2}"