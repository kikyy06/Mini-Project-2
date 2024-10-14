from prettytable import PrettyTable
import os
import sys
os.system ("cls")

def home():
    while True:
        print(f"====== Login ======")
        print(f"====== Organisasi ======")

table = PrettyTable()
table.field_names = ["No Struktur", "Nama Anggota", "Jobdesk"]

# Daftar Anggota
def initial_data():
    table.add_row(["1", "April", "Ketua"])
    table.add_row(["2", "Kikay", "Sekretaris"])
    table.add_row(["3", "Putri", "Bendahara"])
    table.add_row(["4", "Camel", "Kewirausahaan"])
    table.add_row(["5", "Rani", "Humas"])
    table.add_row(["6", "Arey", "Publikasi dokumentasi"])

# Fungsi Login
def login():
    print("=" * 6 + " Selamat Datang di Daftar Jobdesk Organisasi " + "=" * 6)
    print("[1]. Admin")
    print("[2]. Mahasiswa")
    print("[3]. Keluar")
    pilihan = input("Silakan pilih Mode Login: ")

    if pilihan == "1":
        username = input("Masukkan Username Admin: ")
        password = input("Masukkan Password Admin: ")
        if username == "admin" and password == "punyaadmin":
            admin()
        else:
            print("Login gagal, username atau password salah.")
            login()
    elif pilihan == "2":
        username = input("Masukkan Nama Mahasiswa: ")
        password = input("Masukkan Password Mahasiswa: ")
        if username == "mahasiswa" and password == "2409116089":
            mahasiswa(username)
        else:
            print("Login gagal, nama atau password salah.")
            login()
    elif pilihan == "3":
        print("Terima kasih sudah menggunakan program ini")
        sys.exit()
    else:
        print("Pilihan tidak tersedia.")
        login()

# Login untuk Admin
def admin():
    while True:
        print("=" * 6 + " Selamat Datang Admin " + "=" * 6)
        print("[1]. Tambah Anggota")
        print("[2]. Hapus Anggota")
        print("[3]. Lihat Anggota")
        print("[4]. Perbarui Anggota")
        print("[5]. Logout")
        pilihan = input("Pilih Fitur yang Diinginkan: ")

        if pilihan == "1":
            tambah_anggota_admin()
        elif pilihan == "2":
            hapus_anggota()
        elif pilihan == "3":
            lihat_anggota()
        elif pilihan == "4":
            perbarui_anggota()
        elif pilihan == "5":
            print("Anda telah logout dari admin.")
            login()
            sys.exit()
        else:
            print("Pilihan tidak valid, coba lagi.")

#Fungsi Menambahkan Anggota ke Daftar
def tambah_anggota_admin():
    no_struktur = input("Masukkan Nomor Struktur:") 
    nama_anggota = input("Masukkan Nama Anggota Baru:")
    jobdesk = input("Masukkan Jobdesk:")
    table.add_row([no_struktur, nama_anggota,  jobdesk])
    print(f"Anggota {nama_anggota} berhasil ditambahkan")

# Fungsi menghapus anggota
def hapus_anggota():
    lihat_anggota()
    no_struktur = input("Masukkan Nomor Struktur yang mau dihapus: ")

    for row in table.rows:
        if row[0] == no_struktur:
            table.del_row(table.rows.index(row))
            print(f"Anggota dengan nomor {no_struktur} berhasil dihapus.")
            # Memperbarui nomor struktur setelah penghapusan
            for index, row in enumerate(table.rows, start=1):
                row[0] = str(index)
            return
    print("Anggota tidak ditemukan.")

# Fungsi melihat anggota
def lihat_anggota():
    print(table)

# Fungsi memperbarui data anggota
def perbarui_anggota():
    lihat_anggota()
    no_struktur = input("Masukkan Nomor Struktur yang mau diubah: ")
    for row in table.rows:
        if row[0] == no_struktur:
            pilihan = input("Ingin mengubah (Nama/Jobdesk)? ").capitalize()
            if pilihan == "Nama":
                nama_baru = input("Masukkan Nama Baru: ")
                row[1] = nama_baru
            elif pilihan == "Jobdesk":
                jobdesk_baru = input("Masukkan Jobdesk Baru: ")
                row[2] = jobdesk_baru
            print(f"Data anggota dengan nomor {no_struktur} berhasil diperbarui.")
            return
    print("Anggota tidak ditemukan.")

# Fungsi untuk mode Mahasiswa
def mahasiswa(username):
    print(f"Selamat datang {username}, Berikut adalah daftar jobdesk organisasi:")
    lihat_anggota()

    while True:
        print("[1]. Lihat Daftar Anggota")
        print("[2]. Logout")
        print("[3]. Keluar")
        pilihan = input("Silakan pilih apa yang akan dilakukan: ")

        if pilihan == "1":
            lihat_anggota()
        elif pilihan == "2":
            print(f"Anda telah logout.")
            login()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini")
            sys.exit()
        else:
            print("Pilihan tidak valid, coba lagi.")

initial_data()
login()