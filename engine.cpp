#include <fstream>
#include <iostream>
#include <limits>
#include <queue>
#include <sstream>
#include <vector>


using namespace std;

const double INF = numeric_limits<double>::infinity();
double graph[13][13] = {0};

void load_csv() {
  ifstream file("dataJarak.csv");
  string line, val;
  getline(file, line); // Skip header
  while (getline(file, line)) {
    stringstream ss(line);
    string u_str, v_str, d_str;
    getline(ss, u_str, ',');
    getline(ss, v_str, ',');
    getline(ss, d_str, ',');
    graph[stoi(u_str)][stoi(v_str)] = stod(d_str);
  }
}

void dijkstra(int start, int end) {
  load_csv(); // Panggil fungsi load data
  int n = 13;
  vector<double> dist(n, INF);
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
        pq.push({dist[v], v});
      }
    }
  }
  cout << dist[end] << endl; // Mengirim hasil ke Python
}

int main(int argc, char *argv[]) {
  dijkstra(stoi(argv[1]), stoi(argv[2]));
  return 0;
}