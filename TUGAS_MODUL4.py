# Watermark Kelompok XX
# Sistem Kasir dan Inventaris Toko Komputer

# 1. Function Non-Return Type (Tanpa Parameter)
def tampilkan_header_toko():
    print("==========================================")
    print("      TOKO KOMPUTER KELOMPOK XX           ")
    print("==========================================")

# 2. Function Return Type (Berparameter)
def hitung_total_harga(harga_satuan, jumlah_beli):
    total = harga_satuan * jumlah_beli
    # Pengkondisian untuk diskon
    if total >= 5000000:
        diskon = total * 0.10
        print(f"[Info] Selamat! Anda mendapatkan diskon 10% (Rp {int(diskon)})")
        total -= diskon
    elif total >= 2000000:
        diskon = total * 0.05
        print(f"[Info] Selamat! Anda mendapatkan diskon 5% (Rp {int(diskon)})")
        total -= diskon
    return int(total)

# Class untuk menerapkan Method
class SistemKasir:
    def __init__(self):
        self.daftar_barang = {
            "RAM 16GB": {"harga": 800000, "stok": 10},
            "SSD 1TB": {"harga": 1200000, "stok": 5},
            "VGA RTX 4060": {"harga": 5000000, "stok": 3}
        }
        self.total_penjualan_hari_ini = 0

    # 3. Method Non-Return Type (Berparameter)
    def tambah_stok(self, nama_barang, jumlah_tambah):
        if nama_barang in self.daftar_barang:
            self.daftar_barang[nama_barang]["stok"] += jumlah_tambah
            print(f"[Sukses] Stok {nama_barang} berhasil ditambah sebanyak {jumlah_tambah}.")
        else:
            print("[Error] Barang tidak ditemukan dalam inventaris!")

    # 4. Method Return Type (Tanpa Parameter)
    def get_ringkasan_transaksi(self):
        return f"Total akumulasi pendapatan toko hari ini: Rp {self.total_penjualan_hari_ini}"

    def tampilkan_stok(self):
        print("\nDaftar Barang & Stok saat ini:")
        # Perulangan
        for barang, detail in self.daftar_barang.items():
            print(f"- {barang}: Rp {detail['harga']} (Stok: {detail['stok']})")


# Main Program
if __name__ == "__main__":
    kasir = SistemKasir()
    berjalan = True

    tampilkan_header_toko()

    # Perulangan While
    while berjalan:
        print("\n--- MENU UTAMA ---")
        print("1. Lihat Stok Barang")
        print("2. Transaksi Pembelian")
        print("3. Tambah Stok Barang")
        print("4. Lihat Ringkasan Pendapatan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        # Pengkondisian
        if pilihan == "1":
            kasir.tampilkan_stok()
        elif pilihan == "2":
            kasir.tampilkan_stok()
            item = input("Masukkan nama barang yang dibeli: ")
            if item in kasir.daftar_barang:
                jumlah = int(input("Masukkan jumlah unit: "))
                stok_ada = kasir.daftar_barang[item]["stok"]
                
                if jumlah <= stok_ada:
                    harga_satuan = kasir.daftar_barang[item]["harga"]
                    bayar = hitung_total_harga(harga_satuan, jumlah)
                    kasir.daftar_barang[item]["stok"] -= jumlah
                    kasir.total_penjualan_hari_ini += bayar
                    print(f"[Sukses] Total bayar: Rp {bayar}")
                else:
                    print("[Error] Stok tidak mencukupi!")
            else:
                print("[Error] Barang tidak valid!")
        elif pilihan == "3":
            item = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah stok tambahan: "))
            kasir.tambah_stok(item, jumlah)
        elif pilihan == "4":
            ringkasan = kasir.get_ringkasan_transaksi()
            print(f"\n[Ringkasan] {ringkasan}")
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan sistem kasir Kelompok XX.")
            berjalan = False
        else:
            print("[Error] Pilihan menu tidak valid!")