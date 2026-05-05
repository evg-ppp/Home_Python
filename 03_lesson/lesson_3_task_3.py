# Импортировать класс Address и Mailing
from address import Address
from mailing import Mailing

# Создаем  экземпляр класса Address
to_address = Address(
    index="123456",
    city="Москва",
    street="Ленина",
    house="10",
    apartment="15"
)
from_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский",
    house="20",
    apartment="5"
)
# Создаем  экземпляр класса Mailing
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=150,
    track="RU123456789"
    )
# Напечатать информацию об отправлении
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}.Стоимость {mailing.cost} рублей."
    )
