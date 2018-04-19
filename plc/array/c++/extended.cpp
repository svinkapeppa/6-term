#include <iostream>
#include <cstring>
#include <string>

using namespace std;

struct ITextHandler {
  virtual ~ITextHandler() = default;

  virtual string Process(const string &text) const = 0;
};

struct LowercaseHandler : ITextHandler {
  string Process(const string &text) const override {
    auto res = text;
    for (auto &&symb : res) {
      symb = static_cast<char>(tolower(symb));
    }
    return res;
  }
};

struct TitlecaseHandler : ITextHandler {
  string Process(const string &text) const override {
    auto res = text;
    bool isWordStart = true;
    for (char &re : res) {
      if (isWordStart && re != ' ') {
        re = static_cast<char>(toupper(re));
        isWordStart = false;
      } else if (re == ' ') {
        isWordStart = true;
      } else {
        re = static_cast<char>(tolower(re));
      }
    }
    return res;
  }
};

template<typename T>
class Array {
public:
  ~Array();
  void Add(const T &element);
  int Size() const;
  T &operator[](int pos);
  const T &operator[](int pos) const;
  string Apply(const string &text) const;
private:
  static constexpr int initialCapacity = 4;
  static constexpr int loadFactor = 4;
  T *buffer = new T[initialCapacity];
  int size = 0;
  int capacity = initialCapacity;

  void Resize();
};

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
string Array<T>::Apply(const string &text) const {
  auto formated = text;
  for (auto i = 0; i < size; ++i) {
    formated = buffer[i]->Process(formated);
  }
  return formated;
}

template<typename T>
void Array<T>::Resize() {
  capacity *= loadFactor;
  auto *tmp = new T[capacity];
  memcpy(tmp, buffer, size * sizeof(int));
  delete[] buffer;
  buffer = tmp;
}

int main() {
  Array<shared_ptr<ITextHandler>> handlers;
  handlers.Add(make_shared<LowercaseHandler>());
  handlers.Add(make_shared<TitlecaseHandler>());
  cout << handlers.Apply("SaMple teXt") << endl;
  return 0;
}

