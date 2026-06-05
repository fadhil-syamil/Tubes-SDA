import os
import subprocess
import csv
import time
import sys
border = "─" * 60

def load_data():
    data_tempat = {} 
    with open('namaTempat.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data_tempat[int(row['id'])] = {
                "nama": row['namaTempat'],
                "deskripsi": row['deskripsi']
            }
    return data_tempat

data_tempat = load_data()

def show_loading(duration=2):
    print("\nMenghitung Rute dan Estimasi Waktu", end="")
    for _ in range(3):
        time.sleep(duration / 3)
        sys.stdout.write(".")
        sys.stdout.flush()
    print("\n")

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{border}")
    print(f"       SELAMAT DATANG DI JEJAK BANDUNG")
    print(f"   Temukan rute wisata terbaikmu hari ini!")
    print(f"{border}")

    print(f"{'ID':<4} | {'Destinasi Wisata'}")
    print("-" * 30)
    for id_tempat, info in data_tempat.items():
        print(f"{id_tempat:<4} | {info['nama']}")
    
    try:
        print(f"\n{border}")
        start = int(input(">> Masukkan ID Titik Awal : "))
        end = int(input(">> Masukkan ID Tujuan     : "))
        
        if start not in data_tempat or end not in data_tempat:
            print("\n[!] ID tidak ditemukan. Silakan cek kembali.")
            input("\nTekan Enter untuk mencoba lagi...")
            return
        
        if start == end:
            print("\n[!] Titik awal dan tujuan tidak boleh sama.")
            input("\nTekan Enter untuk mencoba lagi...")
            return
        
        print(f"\n{border}")
        print(f"MEMPROSES JEJAK PERJALANAN...")
        print(f"Dari : {data_tempat[start]['nama']} - {data_tempat[start]['deskripsi']}")
        print(f"Ke   : {data_tempat[end]['nama']} - {data_tempat[end]['deskripsi']}")
        print(f"{border}")

        show_loading(1.5)

        process = subprocess.run(['./engine.exe', str(start), str(end)], capture_output=True, text=True)
        hasil = process.stdout.strip().split('\n')

        jarak = float(hasil[0])
        rute = hasil[1]

        print(f"✔ Rute Ditemukan!")
        print(f"Jalur Utama : {rute}")
        print(f"Total Jarak : {jarak:.2f} km")
        print(f"Estimasi    : {int(jarak * 10)} - {int(jarak * 15)} menit perjalanan.")
        
    except Exception as e:
        print(f"\n[!] Terjadi error teknis: {e}")
        input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nIngin mencari jejak lainnya? (y/n): ").lower() != 'y':
            print(f"\n{border}")
            print("Terima kasih telah menggunakan Jejak Bandung!")
            print("Sampai jumpa di perjalanan berikutnya!")
            print(f"{border}\n")
            break