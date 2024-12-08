# Daftar mahasiswa sebagai list of dictionaries
mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data {nama} berhasil ditambahkan.")

# Fungsi untuk menampilkan daftar mahasiswa
def tampilkan():
    if len(mahasiswa) == 0:
        print("Tidak ada data mahasiswa.")
    else:
        print("\nDaftar Mahasiswa:")
        for index, data in enumerate(mahasiswa, 1):
            print(f"{index}. Nama: {data['nama']}, Nilai: {data['nilai']}")

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    global mahasiswa
    mahasiswa = [data for data in mahasiswa if data['nama'] != nama]
    print(f"Data mahasiswa dengan nama {nama} telah dihapus.")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama):
    for data in mahasiswa:
        if data['nama'] == nama:
            print(f"Data mahasiswa {nama}: Nilai saat ini = {data['nilai']}")
            nilai_baru = float(input("Masukkan nilai baru: "))
            data['nilai'] = nilai_baru
            print(f"Data mahasiswa {nama} telah diubah.")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

# Program utama untuk menampilkan menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            ubah(nama)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program utama
menu()
