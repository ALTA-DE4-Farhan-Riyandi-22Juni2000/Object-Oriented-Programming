class HitungHargaKirim:

    harga_standard = 5000

    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    @property
    def hitung_harga_kirim(self):
        volume = self.panjang * self.lebar * self.tinggi
        berat_pembulatan = round(self.berat)
        if volume >= 40 and berat_pembulatan >= 1:
            return self.harga_standard
        else:
            return 0

def main():
    hitung = HitungHargaKirim(5,2,4,1)
    print(hitung.hitung_harga_kirim)

if __name__ == "__main__":
    main()
