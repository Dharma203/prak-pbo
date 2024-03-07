class Tiket:
    def __init__(self, no_tiket, items, total):
        self.no_tiket = no_tiket
        self.items = items
        self.total = total

    def tampilkan_tiket(self):
        print(f"Nomor Tiket : {self.no_tiket}")
        print("Items:")
        for item in self.items:
            print(f"- {item}")
        print(f"Harga Total: Rp{self.total}")

    def __del__(self):
        print(f"Tiket {self.no_tiket} Telah dibeli!")

def tiket_decorator(func):
    def wrapper(self, no_tiket, items, total):
        print(f"Tiket baru diterima: Tiket {no_tiket}")
        func(self, no_tiket, items, total)
    return wrapper

class KikiTravel:
    def __init__(self, nama):
        self.nama = nama
        self.orders = []

    @tiket_decorator
    def place_order(self, no_tiket, items, total):
        new_order = Tiket(no_tiket, items, total)
        self.orders.append(new_order)

    def tampilkan_tiket(self):
        print(f"Orders at {self.nama}:")
        for order in self.orders:
            order.tampilkan_tiket()
            print()



travel = KikiTravel("QuickBite")

travel.place_order(1, ["First Class", "Economy", "Business"], 25000)
travel.place_order(2, ["Business", "Economy"], 10000)

travel.tampilkan_tiket()

del travel