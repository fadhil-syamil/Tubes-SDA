import os
import subprocess
import csv
import time
import sys

border = "─" * 45
spasi = 45

# Membaca daftar nama tempat saja
def load_nama():
    nama_tempat = []
    with open('namaTempat.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nama_tempat.append(row['namaTempat'])
    return nama_tempat

nama_tempat = load_nama()

def show_loading(duration=2):
    animation = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in animation:
            sys.stdout.write(f"\rMenghitung rute tercepat... {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\rMenghitung rute tercepat... Selesai!   \n")

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    judul = "\033[1m   Aplikasi Rekomendasi Wisata Bandung\033[0m"
    print(f"\n{border}\n{judul}\n{border}")
    for i, tempat in enumerate(nama_tempat):
        print(f"{i:2}: {tempat}")

    def print_center(text):
        print(text.center(spasi))
    
    try:
        start = input("\n>> ID Titik Awal (0-12): ")
        end = input(">> ID Tujuan (0-12): ")
        
        print()
        show_loading(1.5) 
        
        # Panggil Engine C++
        process = subprocess.run(['./engine.exe', start, end], capture_output=True, text=True)
        jarak = float(process.stdout.strip())
        
        print()
        print_center("✔ Rute Ditemukan!")
        print(f"{border}")
        print_center(f"Total Jarak: {jarak:.2f} km")
        print_center(f"Estimasi: {int(jarak * 10)} - {int(jarak * 15)} Menit")
    except:
        print("Error: Pastikan engine.exe sudah dikompilasi!")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            print("\n" + border)
            print("Terima kasih telah menggunakan Aplikasi Rekomendasi Wisata Bandung!")
            print("Sampai jumpa di perjalanan Anda berikutnya!")
            print(border + "\n")
            break