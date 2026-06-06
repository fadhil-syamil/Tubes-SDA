#include <fstream>
#include <iostream>
#include <limits>
#include <queue>
#include <sstream>
#include <vector>


using namespace std;

const double INF = numeric_limits<double>::infinity();
vector<string> namaTempat;
double graph[13][13] = {0};

const int kapasitas = 13;

struct stack {
  int top;
  int temp[kapasitas];
} stack;

void createStack() {
  stack.top = -1;
}

int isEmpty() {
  if (stack.top == -1) {
    return 1;
  }
  else {
    return 0;
  }
}

int isFull() {
  if (stack.top == kapasitas -1) {
    return 1;
  }
  else {
    return 0;
  }
}

void push (int data) {
  if (isFull() ==1) {
    cerr << "Maaf, stack sudah penuh" << endl;
  }
  else {
    stack.top++;
    stack.temp[stack.top] = data;
  }
}

void displayStack() {
  if (isEmpty() == 0) {
    cerr << "Menampilkan isi stack" << endl;
    for (int i = stack.top; i >= 0; i--) {
      cerr << "data index stack ke-" << i << " adalah " << stack.temp[i] << endl;
    }
    cerr << endl;
  }
  else {
    cerr << "Maaf, tidak ada data pada stack" << endl;
  }
}

int pop() {
  if (isEmpty() == 0 ) {
    int value = stack.temp[stack.top];
    stack.top--;
    return value;
  }
  else {
    cerr << "Maaf, stack kosong" << endl;
    return -1;
  }
}

int peek()
{
    if(isEmpty() == 0)
    {
        return stack.temp[stack.top];
    }
    else
    {
        return -1;
    }
}

void findStack(int data) {
  int tmp, itmp;
  int ditemukan = 0;
  if (isEmpty() == 1) {
    cerr << "Tidak ada data yang bisa dicari, karena stack kosong" << endl;
  }
  else {
    for (int i = stack.top; i >= 0; i--) {
      if (data == stack.temp[i]) {
        tmp = data;
        itmp = i;
        ditemukan = 1;
        break;
      }
    }
    if (ditemukan == 1) {
      cerr << "Data " << data << " ditemukan di index ke-" << itmp << endl;
    }
    else {
      cerr << "Tidak ada data " << data << " ditemukan pada stack" << endl;
    }
  }
}

void load_csv() {
  ifstream file("dataJarak.csv");
  string line, val;
  getline(file, line);
  while (getline(file, line)) {
    stringstream ss(line);
    string u_str, v_str, d_str;
    getline(ss, u_str, ',');
    getline(ss, v_str, ',');
    getline(ss, d_str, ',');
    graph[stoi(u_str)][stoi(v_str)] = stod(d_str);
  }
}

void load_nama()
{
    ifstream file("namaTempat.csv");

    string line;

    getline(file,line);

    while(getline(file,line))
    {
        stringstream ss(line);

        string id,nama;

        getline(ss,id,',');
        getline(ss,nama,',');

        namaTempat.push_back(nama);
    }
}

void dijkstra(int start, int end) {
  int n = 13;
  vector<double> dist(n, INF);
  vector<int> prev(n, -1);
  dist[start] = 0;
  priority_queue<pair<double, int>, vector<pair<double, int>>,
                 greater<pair<double, int>>>
      pq;
  pq.push({0, start});

  while (!pq.empty()) {
    int u = pq.top().second;
    pq.pop();
    for (int v = 0; v < n; v++) {
      if (graph[u][v] > 0 && dist[u] + graph[u][v] < dist[v]) {
        dist[v] = dist[u] + graph[u][v];
        prev[v] = u;
        pq.push({dist[v], v});
      }
    }
  }

  createStack();
  int cur = end;
  while (cur != -1) {
    push(cur);
    cur = prev[cur];
  }

  string route = "";
  cerr << "\n=== Rute Kunjungan (dari start ke end) ===" << endl;
  while(isEmpty() == 0)
{
    int node = pop();

    route += namaTempat[node];

    if(isEmpty() == 0)
    {
        route += " -> ";
    }
}
  cerr << endl;
  cerr << "===========================================" << endl;
  cout << dist[end] << endl; 
  cout << route << endl; 
}

int main(int argc, char *argv[]) {
  if (argc != 3) {
    cerr << "Usage: engine.exe <start> <end>" << endl;
    return 1;
  }

  load_csv(); 
  load_nama(); 

  dijkstra(stoi(argv[1]), stoi(argv[2]));
  return 0;
}