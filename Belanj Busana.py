print("Selamat Datang, Pilihlah Ukuran Baju yang Anda Inginkan : ")
S = s = 50000
M = m = 65000
L = l = 70000
XL = xl = 75000
ukuranbaju = (input("Ukuran Baju Anda (S,L,M,XL) : "))
if ukuranbaju == "S" or "s":
    print("Harga Baju Ukuran S = Rp", S)
    banyak = int(input("Jumlah Baju : "))
    print("Total Belanjaan Anda = Rp", S * banyak)
    print("Terima Kasih Telah Berbelanja Disini :)")
elif ukuranbaju == "M" or "m":
    print("Harga Baju Ukuran M = Rp", M)
    banyak = int(input("Jumlah Baju : "))
    print("Total Belanjaan Anda = Rp", M * banyak)
    print("Terima Kasih Telah Berbelanja Disini :)")
elif ukuranbaju == "L" or "l":
    print("Harga Baju Ukuran L = Rp", L)
    banyak = int(input("Jumlah Baju : "))
    print("Total Belanjaan Anda = Rp", L * banyak)
    print("Terima Kasih Telah Berbelanja Disini :)")
elif ukuranbaju == "XL" or "xl":
    print("Harga Baju Ukuran XL = Rp", XL)
    banyak = int(input("Jumlah Baju : "))
    print("Total Belanjaan Anda = Rp", XL * banyak)
    print("Terima Kasih Telah Berbelanja Disini :)")
else:
    print("Maaf, Ukuran Baju yang Anda Pilih Tidak Tersedia")
