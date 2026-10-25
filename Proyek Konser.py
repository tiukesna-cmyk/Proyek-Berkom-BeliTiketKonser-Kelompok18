
#sistem Sign in pembuatan akun baru
print("==================================================================")
print("------------------------- Pembuatan Akun -------------------------")
print("==================================================================")
user = str(input("Masukkan Username : "))

while user == (""):
    print("Anda belum memasukkan username yang valid.")
    user = str(input("Masukkan Username : "))

pasw = str(input("Masukkan Password baru (password minimal 8 karakter) = "))

while len(pasw) < 8:
    print("Password tidak memenuhi jumlah minimal karakter.")
    pasw = str(input("Masukkan Password baru (password minimal 8 karakter) = "))

pasw_2 = str(input("Konfirmasi password = "))

while pasw != pasw_2:
    print("Password belum sama.")
    pasw_2 = str(input("Konfirmasi password = "))

print("---------------- ! Akun telah dibuat ! ----------------")

#proses pemesanan tiket
print("==================================================================")
print("--------------- Pemesanan Tiket Konser The Beatles ---------------")
print("==================================================================")
print("Kursi yang tersedia : ")
print("CAT 1 : Rp1.500.000  [SISA 5 KURSI]")
print("CAT 2 : Rp1.200.000  [SISA 4 KURSI]")
print("CAT 3 : Rp1.000.000  [SISA 2 KURSI]")
print("CAT 4 : Rp900.000    [SISA 6 KURSI]")

jnis_tiket = str(input("Masukkan Jenis Kursi yang Anda Ingin Beli  = "))
jmlh_tiket = int(input("Masukkan Jumlah Tiket yang Anda Ingin Beli = "))

#kursi yang tersedia
krsi_CAT1 = [ 'A1' , 'A2', 'A3', 'A4', 'A5']
krsi_CAT2 = [ 'B1' , 'B3', 'B4', 'B5']
krsi_CAT3 = [ 'C2', 'C6']
krsi_CAT4 = [ 'D1', 'D2' , 'D3' , 'D4', 'D5', 'D6']

#cek jika kursi kosong
while (jnis_tiket == ''):
        print("Masukkan jenis kursi yang valid.")
        jnis_tiket = str(input("Masukkan Jenis Kursi yang Anda Ingin Beli  = "))

if (jnis_tiket == 'CAT 1'):
    x = jmlh_tiket*1500000
    print("Total harga tiket = Rp", x)
    print("Kursi yang tersedia = ", krsi_CAT1)
    kursi = str(input("Pilih kursi yang diinginkan = "))
elif (jnis_tiket == 'CAT 2') :
    x = jmlh_tiket*1200000
    print("Total harga tiket = Rp", x)
    print("Kursi yang tersedia = ", krsi_CAT2)
    kursi = str(input("Pilih kursi yang diinginkan = "))
elif (jnis_tiket == 'CAT 3'):
    x = jmlh_tiket*1000000
    print("Total harga tiket = Rp", x)
    print("Kursi yang tersedia = ", krsi_CAT3)
    kursi = str(input("Pilih kursi yang diinginkan = "))
elif (jnis_tiket == 'CAT 4') :
    x = jmlh_tiket*900000
    print("Total harga tiket = Rp", x)
    print("Kursi yang tersedia = ", krsi_CAT4)
    kursi = str(input("Pilih kursi yang diinginkan = "))



print("===========================================================")
print("--------------- Data Pembeli dan Pembayaran ---------------")
print("===========================================================")
nama  = str(input("Nama Lengkap                           = "))
lahir = str(input("Tempat, Tanggal Lahir                  = "))
gender= str(input("Jenis Kelamin                          = "))
nik   = str(input("Masukkan no.KTP                        = "))

#cek kalau nik bener
while (len(nik) != 16):
    print("Tolong masukkan no.KTP yang valid.")
    nik   = str(input("Masukkan no.KTP                        = "))

bayar = int(input("Jumlah yang dibayar (tanpa tanda baca) = "))
sisa = x-bayar

if (sisa < 0):
    sisa = sisa*-1
    print("")
    print("Pembayaran melebihi yang perlu dibayar,  kembalian = Rp", sisa)
    print("")
    print("=========================================================")
    print("------------------------- Struk -------------------------")
    print("=========================================================")
    print("Nama Lengkap          = " , nama)
    print("Tempat, Tanggal Lahir = ", lahir)
    print("Jenis Kelamin         = ", gender)
    print("No. KTP               = ", nik)
    print("Jenis Kursi           = ", jnis_tiket)
    print("NO. Kursi             = ", kursi)
    print("Jumlah Tiket          = ", jmlh_tiket )
    print("Total Pembelian       =  Rp", x)
    print("--------------- Enjoy the Show (＠＾０＾) ---------------")
    print("=========================================================")
elif (sisa > 0):
    print("")
    print("Pembayaran kurang dari yang perlu dibayar,  silahkan membayar = Rp", sisa)
else:
    print("")
    print("---------------- ! Pembayaran berhasil ! ----------------")
    print("")
    print("=========================================================")
    print("------------------------- Struk -------------------------")
    print("=========================================================")
    print("Nama Lengkap          = " , nama)
    print("Username              = " , user)
    print("Tempat, Tanggal Lahir = ", lahir)
    print("Jenis Kelamin         = ", gender)
    print("No. KTP               = ", nik)
    print("Jenis Kursi           = ", jnis_tiket)
    print("NO. Kursi             = ", kursi)
    print("Jumlah Tiket          = ", jmlh_tiket )
    print("Total Pembelian       =  Rp", x)
    print("--------------- Enjoy the Show (＠＾０＾) ---------------")
    print("=========================================================")


