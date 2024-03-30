class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    
    def bersuara(self):
        pass
    
    def makan(self):
        print(f"{self.nama} sedang makan.")
    
    def minum(self):
        print(f"{self.nama} sedang minum.")

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} (kucing) : Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} (anjing) : Guk guk!")

kucing = Kucing("Kinoy", "Betina")
anjing = Anjing("Anjir", "Jantan")

kucing.bersuara()
kucing.makan()
kucing.minum()

print("=========================")

anjing.bersuara()
anjing.makan()
anjing.minum()