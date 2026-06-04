import os
import subprocess
import csv

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
        start = input("\n>> ID Titik Awal: ")
        end = input(">> ID Tujuan: ")
        
        # Panggil Engine C++
        process = subprocess.run(['./engine.exe', start, end], capture_output=True, text=True)
        jarak = float(process.stdout.strip())
        
        print(f"\n✔ Rute Ditemukan!")
        print(f"Total Jarak: {jarak:.2f} km")
        print(f"Estimasi: {int(jarak * 10)} - {int(jarak * 15)} Menit")
    except:
        print("Error: Pastikan engine.exe sudah dikompilasi!")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y': break