def hitung_bil_ganjil(batas_bawah, batas_atas):
    if batas_bawah < 0 or batas_atas < 0:
        print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
        return

    jmlh_ganjil = 0
    for i in range(batas_bawah, batas_atas):
        if i % 2 != 0:
            jmlh_ganjil += i

    print(f"Jumlah bilangan ganjil antara {batas_bawah} dan {batas_atas} adalah: {jmlh_ganjil}")


if __name__ == "__main__":
    batas_bawah = int(input("batas bawah: "))
    batas_atas = int(input("batas atas: "))

    hitung_bil_ganjil(batas_bawah, batas_atas)