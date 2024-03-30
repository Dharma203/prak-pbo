class Bentuk:
    def hitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def hitungLuas(self):
        return 3.14 * self.jari_jari ** 2

def hitung_luas_objek(objek):
    return objek.hitungLuas()

persegi = Persegi(5)
lingkaran = Lingkaran(3)

print("Luas Persegi:", hitung_luas_objek(persegi))
print("Luas Lingkaran:", hitung_luas_objek(lingkaran))