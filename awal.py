import os


nama_tempat = ["Asia Afrika", "Braga", "Gedung Sate", "Dago"]


graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]  
]

def hitung_rute(start, end):
    if start == end:
        return nama_tempat[start]
    
    if graph[start][end] == 1:
        return f"{nama_tempat[start]} -> {nama_tempat[end]}"
    
    for i in range(4):
        if graph[start][i] == 1 and graph[i][end] == 1:
            return f"{nama_tempat[start]} -> {nama_tempat[i]} -> {nama_tempat[end]}"
            
    return "Rute tidak ditemukan (Lokasi terlalu jauh/terputus)"

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
            rute = hitung_rute(start, end)
            print(f"\n✔ Rute Ditemukan!")
            print("----------------------------------------")
            print(f"Status   : Ditemukan")
            print(f"Jalur    : {rute}")
            print(f"Estimasi : 15-20 Menit")
            print("----------------------------------------")
        else:
            print("Input tidak valid! Masukkan angka 0-3.")
    except ValueError:
        print("Input harus berupa angka!")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            print("\nTerima kasih!")
            break