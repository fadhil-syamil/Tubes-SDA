import subprocess
import sys

def main_menu():
    print("=== Bandung Heritage Recommendation ===")
    print("0: Asia Afrika | 1: Braga | 2: Gedung Sate | 3: Dago")
    
    try:
        start = int(input("Masukkan titik awal (0-3): "))
        end = int(input("Masukkan tujuan (0-3): "))
        
        if not (0 <= start <= 3 and 0 <= end <= 3):
            print("Input tidak valid!")
            return

        # Memanggil C++ Engine
        # Asumsi engine sudah dikompilasi menjadi 'engine.exe' atau 'engine'
        cmd = ['./engine', str(start), str(end)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Hasil Navigasi:")
            print(result.stdout.strip())
        else:
            print("Error saat menjalankan engine.")
            
    except ValueError:
        print("Input harus angka!")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("\nLagi? (y/n): ") != 'y':
            break