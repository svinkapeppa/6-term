#include <vector>
#include <iostream>

class ICallback {
public:
  ICallback() {}

  ~ICallback() {}

  virtual void discover_vertex(int vertex) = 0;

  virtual void finish_vertex(int vertex) = 0;
};

class ExtendedCallback : public ICallback {
public:
  void discover_vertex(int vertex);

  void finish_vertex(int vertex);
};

class Callback : public ICallback {
public:
  void discover_vertex(int vertex);

  void finish_vertex(int vertex);
};

void dfs(std::vector<std::vector<int>> graph, int start, ICallback &callback, std::vector<int> &visited);

int main() {
  int n, m, x;
  std::vector<std::vector<int>> graph;
  Callback cb;
  std::vector<int> visited;

  std::cin >> n;
  visited.resize(n, 0);
  for (auto i = 0; i < n; ++i) {
    std::vector<int> tmp;
    std::cin >> m;
    for (auto j = 0; j < m; ++j) {
      std::cin >> x;
      tmp.push_back(x);
    }
    graph.push_back(tmp);
  }

  dfs(graph, 0, cb, visited);
  return 0;
}

void dfs(std::vector<std::vector<int>> graph, int start, ICallback &callback, std::vector<int> &visited) {
  visited[start] = 1;
  callback.discover_vertex(start);
  for (auto vertex : graph[start]) {
    if (visited[vertex] == 0) {
      dfs(graph, vertex, callback, visited);
    }
  }
  callback.finish_vertex(start);
}

void Callback::discover_vertex(int vertex) {
  std::cout << "[*] " << vertex << std::endl;
}

void Callback::finish_vertex(int vertex) {
  std::cout << "[x] " << vertex << std::endl;
}

void ExtendedCallback::discover_vertex(int vertex) {
  std::cout << "Discover vertex " << vertex << std::endl;
}

void ExtendedCallback::finish_vertex(int vertex) {
  std::cout << "Finish vertex " << vertex << std::endl;
}