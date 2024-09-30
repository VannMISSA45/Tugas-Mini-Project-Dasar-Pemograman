nama = str(input("Silahkan Masukkan Nama: "))
nim = str(input("Silahkan Masukkan Program Studi: "))
prodi = int(input("Masukkan NIM: "))
print(f"HALO, {nama}! ")

while True:
    gaji_karyawan = float(input("Masukkan gaji karyawan selama bekerja; "))
    jam_kerja= int(input("Masukkan jumlah waktu kerja anda: "))

    total_gaji_karyawan = jam_kerja * gaji_karyawan

    if jam_kerja> 160:
        bonus =  total_gaji_karyawan * 0.10
        jumlah_bonus = total_gaji_karyawan + bonus
        print("Selamat anda mendapatkan bonus kerja 10%")
        print(f"Jadi jumlah bonus gaji yang diterima: Rp {jumlah_bonus}")
    else:
        print("Maaf anda belum dapat menerima bonus")
        print(f"jadi jumlah gaji yang diterima: Rp {total_gaji_karyawan}")

    perulangan = input("Ingin menghitung jumlah jam kerja anda kembali? (yes/no) ")
    if perulangan != "yes":
        break