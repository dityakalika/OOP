from Geometri.bangun_ruang import BangunRuang # package geometri, file bangun_ruang dan fungsi BangunRuang
from Geometri.rumus import PersegiPanjang, Segitiga

print('Program OOP')

p1 = PersegiPanjang(10, 4)
print(p1.info())
print(p1.luas())

s1 = Segitiga(4, 6)
print(s1.info())
print(s1.luas())

print('\nMembuat object dari class BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.luas())
# hasil akan None karena pake pass

# Polymorphisme : Respon object yang berbeda terhadap pemanggilan method yang sama.

print('\nPolymorphisme')
list_bangun_ruang = []
list_bangun_ruang.append(p1)
list_bangun_ruang.append(s1)

for a in list_bangun_ruang:
    print(a.info())

# hasil nya akan berbeda beda walau method penulisan sama