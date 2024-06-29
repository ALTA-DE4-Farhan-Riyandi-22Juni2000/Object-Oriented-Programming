class Kalkulator:

  def __init__(self, angka1, angka2):
    self.a1 = angka1
    self.a2 = angka2

  @property
  def penjumlahan(self):
    return self.a1 + self.a2

  @property
  def pengurangan(self):
    return self.a1 - self.a2

  @property
  def perkalian(self):
    return self.a1 * self.a2

  @property
  def pembagian(self):
    return round(self.a1 / self.a2)
  

def main():
  penjumlahan = Kalkulator(3,4)
  pengurangan =  Kalkulator(15,4)
  perkalian = Kalkulator(10,10)
  pembagian = Kalkulator(12,3)
  
  print("penjumlahan: ",penjumlahan.penjumlahan)
  print("pengurangan: ",pengurangan.pengurangan)
  print("perkalian: ",perkalian.perkalian)
  print("pembagian: ",pembagian.pembagian)

if __name__ == "__main__":
    main()