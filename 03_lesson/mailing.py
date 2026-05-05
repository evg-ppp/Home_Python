# Объявить класс
class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address  # тип данных Address
        self.from_address = from_address  # тип данных Address
        self.cost = cost  # тип данных число
        self.track = track  # тип данных строка

    def __str__(self):
        return (
            f"Mailing to: {self.to_address}, "
            f"from: {self.from_address}, "
            f"cost: {self.cost}, track: {self.track} "
            )
