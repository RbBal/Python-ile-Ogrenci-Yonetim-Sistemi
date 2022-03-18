import time

class Ogrenci:
    def __init__(self,ad,soyAd,cinsiyet,dogumTarihi,tcNo,il,okulAdi,okulNo,okulSinif):
        self.ad = ad
        self.soyAd = soyAd
        self.cinsiyet = cinsiyet
        self.dogumTarihi = dogumTarihi
        self.tcNo = tcNo
        self.il = il
        self.okulAdi = okulAdi
        self.okulNo =okulNo
        self.okulSinif = okulSinif

    def bilgiKontrol(self):
        try:
            with open("db/"+self.okulAdi+".txt","r+") as okul:
                veri = okul.read()
                if("$"+self.okulNo in veri or "!"+self.tcNo in veri):
                    return False
                else:
                    return True
        except FileNotFoundError:
            return True


    def bilgileriKaydet(self):
        with open("db/"+self.okulAdi+".txt","a",encoding="utf-8") as okul:
            okul.write(f"{self.ad},{self.soyAd},{self.cinsiyet},{self.dogumTarihi},!{self.tcNo},{self.il},{self.okulAdi},${self.okulNo},{self.okulSinif},\n")


def ogrenciEkle():
    ad = input("Ad: ")
    soyAd = input("Soyad: ")
    cinsiyet = input("Cinsiyet: ")
    dogumTarihi = input("Doğum Tarihi (gg/ay/yıl): ")
    tcNo = input("T.C no: ")
    il = input("Kayıtlı olduğu il: ")
    okulAdi = input("Okulunun Adı: ")
    okulNo = input("Okul numarası: ")
    okulSinif = input("Sınıfı: ")

    ogrenci = Ogrenci(ad,soyAd,cinsiyet,dogumTarihi,tcNo,il,okulAdi,okulNo,okulSinif)
    if(ogrenci.bilgiKontrol()):
        ogrenci.bilgileriKaydet()
    else:
        print(f"{okulAdi} okulunda {okulNo} numaralı öğrenci mevcut")


def ogrenciBulma():
    okulAd = input("Bilgilerini Düzenlemek istediğiniz öğrencinin okulu: ")
    okulNo = input("Bilgilerini Düzenlemek istediğiniz öğrencinin okul numarası: ")
    try:
        with open("db/"+okulAd+".txt","r") as okul:
            veri = okul.read()
        if("$"+okulNo in veri):
            print("Öğrenci bulundu")
            ogrenciDuzenleme(okulAd,okulNo)
        else:
            print(f"{okulNo} numaralı bir öğrenci kayıtlı değil")
    except FileNotFoundError:
        print(f"{okulAd} okulu kayıtlı değil")

def ogrenciDuzenleme(okulAd,okulNo):
    with open("db/"+okulAd+".txt","r",encoding="utf-8") as okul:
        satirlar = okul.readlines()
        for i in satirlar:
            if "$"+okulNo in i:
                hedefIndex = satirlar.index(i)                          
        satirlar.pop(hedefIndex)
    with open("db/"+okulAd+".txt","w",encoding="utf-8") as okul:
        okul.writelines(satirlar)
    print("Ögrencinin bilgileri temizlendi.")
    ogrenciEkle()   #Düzenlenecek öğrencinin bilgileri silinip yeni bilgiler dosyanın sonuna ekleniyor

def ogrencileriListele():
    veriListe = []
    satir = "AD | SOYAD | CİNSİYET | DOĞUM TARİHİ | T.C NO | KAYITLI İL | OKUL ADI | OKUL NO | SINIF |\n-----------------------------------------------------------------------------------------\n"

    okulAd = input("Listelemek istediğiniz okul: ")
    try:
        with open("db/"+okulAd+".txt","r+",encoding="utf-8") as okul:
            veriler = okul.readlines()
            for i in veriler:
                veri = i.split(',')
                veriListe.append(veri[:-1])

    except FileNotFoundError:
        print(f"{okulAd} isminde bir okul kayıtlı değil.")

    for i in veriListe:
        i[4] = i[4][1:]
    for i in veriListe:
        i[7] = i[7][1:]

    for i in veriListe:
        for j in i:
            satir = satir + j +" | "
        satir = satir+"\n"
    print(satir)

    istek = input("Listeyi kaydetmek istiyor musun? e/h :")

    if(istek == "e"):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open("Lists/"+timestr+".txt","a",encoding="utf-8") as liste:
            liste.write(satir)


while True:
    print(
    """
    ###########################
    | Öğrenci Yönetim Sistemi |
    |                         |
    |                    rbal |
    ###########################

    1-) Öğrenci Ekle
    2-) Öğrenci Bilgilerini Düzenle
    3-) Öğrencileri Listele
    4-) Çıkış
    """
    )
    secim = input()

    if secim == "1":
        ogrenciEkle()
    elif secim == "2":
        ogrenciBulma()
    elif secim == "3":
        ogrencileriListele()
    elif secim == "4":
        break
    else:
        print("Hatalı Seçim Numarası")