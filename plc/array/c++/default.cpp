#include <iostream>
#include <cstring>

template<typename T>
class Array {
public:
  ~Array();
  void Add(const T &element);
  int Size() const;
  T &operator[](int pos);
  const T &operator[](int pos) const;
private:
  static constexpr int initialCapacity = 4;
  static constexpr int loadFactor = 2;
  T *buffer = new T[initialCapacity];
  int size = 0;
  int capacity = initialCapacity;

  void Resize();
};

int main() {
  Array<int> arr;
  for (int i = 0; i < 10; ++i) {
    arr.Add(i);
  }
  for (int i = 0; i < arr.Size(); ++i) {
    std::cout << arr[i] << std::endl;
  }
  return 0;
}

template<typename T>
int Array<T>::Size() const {
  return size;
}

template<typename T>
T &Array<T>::operator[](int pos) {
  return buffer[pos];
}

template<typename T>
const T &Array<T>::operator[](int pos) const {
  return buffer[pos];
}

template<typename T>
Array<T>::~Array() {
  size = 0;
  capacity = initialCapacity;
  delete[] buffer;
}

template<typename T>
void Array<T>::Add(const T &element) {
  if (size >= capacity) {
    Resize();
  }
  buffer[size] = element;
  ++size;
}

template<typename T>
void Array<T>::Resize() {
  capacity *= loadFactor;
  auto *tmp = new T[capacity];
  memcpy(tmp, buffer, size * sizeof(int));
  delete[] buffer;
  buffer = tmp;
}
