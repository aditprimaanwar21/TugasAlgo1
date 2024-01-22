class BidangDatar:
    luas = None
    jenis = None


def luas_segitiga():
    print()
    print("Luas Segitiga")
    alas = int (input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = 0.5 * alas * tinggi

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "Segitiga"

    return bidang_datar

def Luas_persegi_panjang():
    bidang_datar = "persegi panjang"
    print()
    print("Luas persegi panjang")
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    luas = panjang * lebar

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "persegi panjang"

    return bidang_datar

def luas_lingkaran():
    bidang_datar ="lingkaran"
    print()
    print("luas lingkaran")
    jarijari = int(input("masukkan jari-jari: "))
    luas = 3.14 * jarijari * jarijari

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "lingkaran"

    return bidang_datar

def luas_jajar_genjang():
    bidang_datar = "jajargenjang"
    print()
    print("luas jajar genjang")
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = alas * tinggi

    bidang_datar = BidangDatar()
    bidang_datar.luas = luas
    bidang_datar.jenis = "jajargenjang"

    return bidang_datar



if __name__ == "__main__":

    while True:
        print("Menu")
        print("====================")
        print("1. Luas segitiga")
        print("2. Luas persegi panjang")
        print("3. Luas lingkaran")
        print("4. Luas jajargenjang")
        print("5. Keluar")
        menu = int(input("pilih menu: "))

        if menu == 5:
            break

        if menu == 1: 
            bidang_datar = luas_segitiga()
        elif menu == 2:
            bidang_datar = Luas_persegi_panjang()
        elif menu == 3:
            bidang_datar = luas_lingkaran()
        elif menu == 4:
            bidang_datar = luas_jajar_genjang()
        
        print("luas {} adalah: {}".format(bidang_datar.jenis, bidang_datar.luas))
        print()