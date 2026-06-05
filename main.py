import os
import subprocess
import csv

border = "─" * 45

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

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{border}\n   Aplikasi Rekomendasi Wisata Bandung\n{border}")
    for id_tempat, info in data_tempat.items():
        print(f"{id_tempat:2}: {info['nama']}")
    
    try:
        start = int(input("\n>> ID Titik Awal: "))
        end = int(input(">> ID Tujuan: "))
        
        if start not in data_tempat or end not in data_tempat:
            print("ID Titik tidak valid!")
            return
        
        if start == end:
            print("Titik Awal dan Tujuan tidak boleh sama!")
            return
        
        print(f"\n--- Detail Lokasi ---")
        print(f"Awal  : {data_tempat[start]['nama']} ({data_tempat[start]['deskripsi']})")
        print(f"Tujuan: {data_tempat[end]['nama']} ({data_tempat[end]['deskripsi']})")
        
        # Panggil Engine C++
        process = subprocess.run(['./engine.exe', str(start), str(end)], capture_output=True, text=True)
        hasil = process.stdout.strip().split('\n')

        jarak = float(hasil[0])
        rute = hasil[1]

        print(f"\n✔ Rute Ditemukan!")
        print(f"Rute: {rute}")
        print(f"Total Jarak: {jarak:.2f} km")
        print(f"Estimasi: {int(jarak * 10)} - {int(jarak * 15)} Menit")
        
    except Exception as e:
        print("Terjadi error:", e)

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            print("\n" + border)
            print("Terima kasih telah menggunakan Aplikasi Rekomendasi Wisata Bandung!")
            break