user_login = ("ser")
user_pass = ("qwe123")

login = input("Login: ")
Password = input("Password: ")

if (login == user_login) and (Password == user_pass):
    print("open")
else:
    print("close")

crit1 = ("red")
crit2 = ("lock")

color = input("Color: ")
feature = input("Feature: ")

if (color == crit1) or (feature == crit2):
    print("buy it!")
else:
    print("search")