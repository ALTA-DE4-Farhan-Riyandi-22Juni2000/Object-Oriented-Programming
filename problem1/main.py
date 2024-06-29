from abc import ABC, abstractmethod
import math

class BangunDatar(ABC):

  @abstractmethod
  def luas(self):
    pass

  @abstractmethod
  def keliling(self):
    pass

class Persegi(BangunDatar):

  def __init__(self, sisi):
    self.sisi = sisi

  @property
  def luas(self):
    return self.sisi * self.sisi

  @property
  def keliling(self):
    return 4 * self.sisi

class Segitiga(BangunDatar):

  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi

  @property
  def luas(self):
    return int((self.alas * self.tinggi) / 2)

  @property
  def keliling(self):
    self.sisi_miring = math.sqrt(self.alas**2 + self.tinggi**2)
    return int(self.alas + self.tinggi + self.sisi_miring)

class PersegiPanjang(BangunDatar):
  def __init__(self, panjang, lebar):
    self.panjang = panjang
    self.lebar = lebar

  @property
  def luas(self):
    return self.panjang * self.lebar

  @property
  def keliling(self):
    return (self.panjang + self.lebar) * 2


def main():
  persegi = Persegi(4)
  segitiga = Segitiga(3,4)
  persegi_panjang = PersegiPanjang(7,8)

  print("Luas")
  print("Persegi:",persegi.luas)
  print("Segitiga:", segitiga.luas)
  print("Persegi Panjang:", persegi_panjang.luas)

  print("kelling:")
  print("Persegi",persegi.keliling)
  print("Segitiga:", segitiga.keliling)
  print("Persegi Panjang:", persegi_panjang.keliling)

if __name__ == "__main__":
    main()
