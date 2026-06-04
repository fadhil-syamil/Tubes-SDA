import os

nama_tempat = ["Asia Afrika", "Braga", "Gedung Sate", "Dago"]


graph_real = [
    [0, 0.8, 4.5, 5.2], 
    [0.8, 0, 4.0, 4.8], 
    [4.5, 4.0, 0, 3.5], 
    [5.2, 4.8, 3.5, 0]  
]

def hitung_rute(start, end):
    if graph_real[start][end] > 0:
        return graph_real[start][end], f"{nama_tempat[start]} -> {nama_tempat[end]}"
    
    for i in range(4):
        if graph_real[start][i] > 0 and graph_real[i][end] > 0:
            jarak = graph_real[start][i] + graph_real[i][end]
            return jarak, f"{nama_tempat[start]} -> {nama_tempat[i]} -> {nama_tempat[end]}"
            
    return 0, "Rute tidak ditemukan"

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("========================================")
    print("   BANDUNG HERITAGE RECOMMENDATION      ")
    print("========================================")
    print(" 0: Asia Afrika | 1: Braga")
    print(" 2: Gedung Sate  | 3: Dago")
    print("----------------------------------------")
    
    try:
        start = int(input(">> Masukkan ID Titik Awal: "))
        end = int(input(">> Masukkan ID Tujuan: "))
        
        if 0 <= start <= 3 and 0 <= end <= 3:
            print("\nMencari rute terbaik...")
            jarak, rute = hitung_rute(start, end)
            print(f"\n✔ Rute Ditemukan!")
            print("----------------------------------------")
            print(f"Jalur        : {rute}")
            print(f"Total Jarak  : {jarak} km")
            print(f"Estimasi     : {int(jarak * 10)} - {int(jarak * 15)} Menit")
            print("----------------------------------------")
        else:
            print("Input tidak valid! Masukkan angka 0-3.")
    except ValueError:
        print("Input harus berupa angka!")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            break