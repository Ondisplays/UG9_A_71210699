#Harga makanan
ikan = 25000
es = 6000
rujak = 8000

print("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")
ib = int(input("IKAN BAKAR      Rp 25,000,00:   "))
ed = int(input("ES DOGER        Rp 6,000,00 :   "))
rc = int(input("RUJAK CINGUR    Rp 8,000,00 :   "))
print("=====TOTAL=====")

#Total makanan
h1 = int(ikan) * ib
h2 = int(es) * ed
h3 = int(rujak) * rc

print("TOTAL IKAN BAKAR         : Rp " + str(h1))
print("TOTAL ES DOGER           : Rp " + str(h2))
print("TOTAL RUJAK CINGUR       : Rp " + str(h3))

#Jumlah keseluruhan
total = h1 + h2 + h3

print("Jumlah total biaya yang harus dibayar adalah Rp " + str(total))
