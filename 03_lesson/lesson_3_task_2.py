# Импортировать класс User
from smartphone import Smartphone


class Smartphone:
    def __init__(self, phone_brand, phone_model, subscriber_number=('+79…')):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number
    # Объявить переменную
    catalog = []  # Создаем пустой список

    phone1 = Smartphone("Samsung", "S26", "+79100112233")
    catalog.append(phone1)
    phone2 = Smartphone("LG", "G7", "+79001001122")
    catalog.append(phone2)
    phone3 = Smartphone("Huawei", "nova 14 pro", "+79003221233")
    catalog.append(phone3)
    phone4 = Smartphone("Xiaomi", "Redmi Note 14S", "+79231002211")
    catalog.append(phone4)
    phone5 = Smartphone("Honor", "X5c", "+79252545789")
    catalog.append(phone5)

    # Наполнить список пятью разными экземплярами класса Smartphone
    for phone in catalog:
        print(f"{phone.phone_brand} - {phone.phone_model}"
              f"{phone.subscriber_number}")
