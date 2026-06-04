import os

border = "─" * 45
spasi = 45

nama_tempat = [
    "Gedung Sate",                  # 0
    "Braga",                        # 1
    "Museum KAA",                   # 2
    "Museum Geologi",               # 3
    "Gereja Katedral",              # 4
    "Hotel Savoy Homann",           # 5
    "Gedung Indonesia Menggugat",   # 6
    "Paris Van Java",               # 7
    "Villa ISOLA",                  # 8
    "Tahura Ir. H. Djuanda",        # 9
    "Dago Dreampark",               # 10
    "Observatorium Bosscha",        # 11
    "Selasar Sunaryo Art Space"     # 12
]

graph_real = [
    [0.0, 3.5, 0.0, 0.45, 0.0, 0.0, 0.0, 0.0, 0.0, 6.3, 0.0, 0.0, 0.0], # 0
    [3.5, 0.0, 0.35, 0.0, 0.7, 1.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 1
    [0.0, 0.35, 0.0, 0.0, 0.0, 0.16, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 2
    [0.45, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 3
    [0.0, 0.7, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 4
    [0.0, 1.3, 0.16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], # 5
    [0.0, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 3.7, 0.0, 0.0, 0.0, 0.0, 0.0], # 6
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.7, 0.0, 3.6, 7.1, 7.9, 0.0, 0.0], # 7
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.6, 0.0, 0.0, 0.0, 7.0, 0.0], # 8
    [6.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.1, 0.0, 0.0, 0.0, 0.0, 0.0], # 9
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.9, 0.0, 0.0, 0.0, 0.0, 4.4], # 10
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0], # 11
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.4, 0.0, 0.0]  # 12
]

def hitung_rute(start, end):
    if graph_real[start][end] > 0:
        return graph_real[start][end], f"{nama_tempat[start]} -> {nama_tempat[end]}"
 
    for i in range(len(nama_tempat)):
        if graph_real[start][i] > 0 and graph_real[i][end] > 0:
            jarak = graph_real[start][i] + graph_real[i][end]
            return jarak, f"{nama_tempat[start]} -> {nama_tempat[i]} -> {nama_tempat[end]}"
            
    return 0, "Rute tidak ditemukan (perlu lebih banyak data transit)"

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{border}")
    print("Selamat Datang di Aplikasi Rekomendasi ".center(spasi))
    print("Tempat Wisata Sejarah Bandung".center(spasi))
    print(f"{border}")
    print("\nDaftar Tempat Wisata:\n")
    for i, tempat in enumerate(nama_tempat):
        print(f"{i:2}: {tempat}")
    print(f"{border}")
    
    try:
        start = int(input(">> Masukkan ID Titik Awal (0-12): "))
        end = int(input(">> Masukkan ID Tujuan (0-12): "))
        
        if 0 <= start < len(nama_tempat) and 0 <= end < len(nama_tempat):
            print("\nMencari rute terbaik...")
            jarak, rute = hitung_rute(start, end)
            print(f"\n✔ Rute Ditemukan!")
            print("----------------------------------------")
            print(f"Jalur        : {rute}")
            print(f"Total Jarak  : {jarak} km")
            print(f"Estimasi     : {int(jarak * 10)} - {int(jarak * 15)} Menit")
            print("----------------------------------------")
        else:
            print("Input tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nCari lagi? (y/n): ").lower() != 'y':
            break