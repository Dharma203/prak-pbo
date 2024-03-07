class Mahasiswa:

    def _init_(self, nim, nama, angkatan, isMahasiswa=None):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        if isMahasiswa == None:
            self.isMahasiswa = True
        else:
            self.isMahasiswa = isMahasiswa
5
    def set_nama(self, __nama):
        self.nama = nama

    def set_nim(self, __nim):
        self.nim = nim

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def _str_(self):
        return f'nama : {self._nama}\nnim : {self._nim}\nangkatan : {self.angkatan}\nmahasiswa : {self.is_mahasiswa_aktif()}'

    def is_mahasiswa_aktif(self):
        if self.isMahasiswa == True:
            return "Mahasiswa aktif"
        else:
            return "Mahasiswa tidak aktif"

    def bandingkan(self, other):
        if self.angkatan > other.angkatan:
            return f'{self._nama} senior dari {other._nama}'
        elif self.angkatan < other.angkatan:
            return f'{self._nama} junior dari {other._nama}'
        else:
            return f'{self._nama} dan {other._nama} di angkatan yang sama'
        
    def kapan_lulus(self):
        return f'{self.get_nama()} harusnya lulus tahun {self.angkatan + 4}'
      


mhs1 = Mahasiswa(122140203, "Dharma", 2020, True)
mhs2 = Mahasiswa(122140204, "Geraldo", 2020)

print(mhs1)
print(mhs2)

print(mhs1.bandingkan(mhs2))
print(mhs1.kapan_lulus())