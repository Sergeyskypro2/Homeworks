from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S 21 Ultra", "+79994445566"),
    Smartphone("Iphone", "16 Pro", "+79991112233"),
    Smartphone("Motorola", "Razer", "+79801123333"),
    Smartphone("Honor", "12 Pro", "+79100002233"),
    Smartphone("Huawei", "Nova", "+79601472536")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")