from Geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang): # BangunRuang dalam kurung menandakan class turunan
    def __init__(self, p, l):
        # __init__ () fungsi yang dipanggil pertama kali dijalankan sebelum method yang lain
        self.p = p
        self.l = l

    def info(self):
        print("Modal menghitung rumus persegi panjang dengan panjang =", self.p, "dan lebar =", self.l)

    def luas(self):
        return self.p * self.l


class Segitiga(BangunRuang): # BangunRuang dalam kurung menandakan class turunan
    def __init__(self, a, t):
        # __init__ () fungsi yang dipanggil pertama kali dijalankan sebelum method yang lain
        self.a = a
        self.t = t

    def info(self):
        print("Modal menghitung segitiga dengan alas =", self.a, "dan tinggi =", self.t)

    def luas(self):
        return self.a * self.t / 2

