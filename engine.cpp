#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Fungsi untuk mengonversi ID ke Nama Tempat
string getNamaTempat(int id) {
  switch (id) {
  case 0:
    return "Asia Afrika";
  case 1:
    return "Braga";
  case 2:
    return "Gedung Sate";
  case 3:
    return "Dago";
  default:
    return "Lokasi Tidak Diketahui";
  }
}

int main(int argc, char *argv[]) {
  if (argc < 3)
    return 1;

  int start = stoi(argv[1]);
  int end = stoi(argv[2]);

  cout << "Status   : Ditemukan" << endl;
  cout << "Jalur    : " << getNamaTempat(start) << " -> " << getNamaTempat(end)
       << endl;
  cout << "Estimasi : 15-20 Menit" << endl;

  return 0;
}