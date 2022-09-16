class Calisanlar():
    calisanlar_listesi = []

    def __init__(self, isim, soyisim, maas, departman):
        self.isim       = isim
        self.soyisim    = soyisim
        self.maas       = maas
        self.departman  = departman
        self.bilgileri_kaydet()

    def bilgileri_kaydet(self):
        self.calisanlar_listesi.append(self.isim)
        self.calisanlar_listesi.append(self.soyisim)
        self.calisanlar_listesi.append(self.maas)
        self.calisanlar_listesi.append(self.departman)

    def bilgileri_goster(self):
        print(self.calisanlar_listesi)

calisan_1 = Calisanlar("Mert", "Kaya", 6500, "Yazılım Geliştirme")

calisan_1.bilgileri_goster() #örnek üzerinden örnek çağırıldı ve çalışır
#Calisanlar.bilgileri_goster() hata verir


#eğer çrnek üzerinden sınıfı çağırırsak çalışmaz bunu gidermek için @classmethod kullanırız,
# böylece sınıfta yapılan her değişilik örneklemi de etkiler

class Calisanlar():
    calisanlar_listesi = []

    def __init__(self, isim, soyisim, maas, departman):
        self.isim       = isim
        self.soyisim    = soyisim
        self.maas       = maas
        self.departman  = departman
        self.bilgileri_kaydet()

    def bilgileri_kaydet(self):
        self.calisanlar_listesi.append(self.isim)
        self.calisanlar_listesi.append(self.soyisim)
        self.calisanlar_listesi.append(self.maas)
        self.calisanlar_listesi.append(self.departman)

    @classmethod
    def bilgileri_goster(cls):  #cls yazmak zorundayız
        print(cls.calisanlar_listesi)

calisan_1 = Calisanlar("Mert", "Kaya", 6500, "Bilgi İşlem")

calisan_1.bilgileri_goster() #örnekte çağırma

Calisanlar.bilgileri_goster() #sınıfta çağırma

"""
Biz, hem sınıf adı üzerinden hem de örneklem adı üzerinden ulaşabileceğimiz bir metot yazsak
 ve bu metodun sınıf içinde herhangi bir değişikliğe neden olmasını istemesek ama aynı zamanda 
 sınıfa ait olmasını istersek bu işlemi nasıl yapabiliriz?
Bu işlemi yapabilmek için @staticmethod dekoratörünü kullanabiliriz.
 Bu dekoratöre de tıpkı @classmethod gibi hem sınıf adıyla hem de örneklem adıyla ulaşabiliriz.
  Statik metodlarda parantez içinde herhangi bir anahtar sözcük (self ya da cls) kullanılmamaktadır.
Aşağıdaki metodu incelediğimizde calisanlara prim vermek için kullanılabilecek
 sabit bir değer belirleyip bu metodun döndürmüş olduğu 0.12 değerini istediğimiz şekilde kullanabiliriz.
  Örnek olarak her ay çalışanlarımıza maaşlarına ek olarak prim ekleyebiliriz.
"""

@staticmethod
def prim_katsayisi():
    return 0.12
