from abc import ABC, abstractmethod
from math import pi

class BangunRuang(ABC):

  @abstractmethod
  def volume(self):
    pass

class Kubus(BangunRuang):

  def __init__(self, sisi):
    self.sisi = sisi

  @property
  def volume(self):
    return self.sisi ** 3

class Balok(BangunRuang):

  def __init__(self, panjang, lebar, tinggi):
    self.panjang = panjang
    self.lebar = lebar
    self.tinggi = tinggi

  @property
  def volume(self):
    return self.panjang * self.lebar * self.tinggi

class Tabung(BangunRuang):

  def __init__(self, jari_jari, tinggi):
    self.jari_jari = jari_jari
    self.tinggi = tinggi

  @property
  def volume(self):
    return round(pi * self.jari_jari ** 2) * self.tinggi
  

def main():
  kubus = Kubus(10)
  balok = Balok(3,6, 10)
  tabung = Tabung(7,10)
  
  print("volume")
  print("Kubus: ",kubus.volume)
  print("Balok: ",balok.volume)
  print("Tabung: ",tabung.volume)

if __name__ == "__main__":
    main()