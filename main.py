import os
import subprocess
import csv
from tracemalloc import start

border = "─" * 45

# Membaca daftar nama tempat saja
def load_nama():
    nama_tempat = []
    with open('namaTempat.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nama_tempat.append(row['namaTempat'])
    return nama_tempat

nama_tempat = load_nama()

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{border}\n   Aplikasi Rekomendasi Wisata Bandung\n{border}")
    for i, tempat in enumerate(nama_tempat):
        print(f"{i:2}: {tempat}")
    
    try:
        start = int(input("\n>> ID Titik Awal: "))
        end = int(input(">> ID Tujuan: "))
        
        if start < 0 or start >= len(nama_tempat):
            print("ID Titik tidak valid!")
            return

        if end < 0 or end >= len(nama_tempat):
            print("ID tidak valid!")
            return
        
        if start == end:
            print("Titik Awal dan Tujuan tidak boleh sama!")
            return
        
        # Panggil Engine C++
        process = subprocess.run(['./engine.exe', str(start), str(end)], capture_output=True, text=True)
        hasil = process.stdout.strip().split('\n')

        jarak = float(hasil[0])
        rute = hasil[1]

        if process.stderr:
            print(" ")
            print(process.stderr)
        
        print(f"\n✔ Rute Ditemukan!")
        print(f"Rute: {rute}")
        print(f"Total Jarak: {jarak:.2f} km")
        print(f"Estimasi: {int(jarak * 10)} - {int(jarak * 15)} Menit")
    except Exception as e:
        print("Terjadi error:")
        print(e)

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            print("\n" + border)
            print("Terima kasih telah menggunakan Aplikasi Rekomendasi Wisata Bandung!")
            print("Sampai jumpa di perjalanan Anda berikutnya!")
            print(border + "\n")
            break