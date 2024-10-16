from address import Address
from mailing import Mailing

to_address = Address("607650", "Kstovo", "Ostrovskovo", "4", "1")
from_address = Address("123456", "Bor", "Neklydovo", "1", "4")
mailing = Mailing(from_address, to_address, "1200", "#1244qw2")
print(mailing)