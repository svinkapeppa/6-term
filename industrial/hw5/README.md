# Задание №5

## Формулировка
Привести примеры антипаттернов в своих проектах.

### God - class
Я делал для знакомого лабораторную: суть заключалась в считывании данных с файла (измерения со спутников), обработки и выписывания результатов.
Сначала я написал программу, которая просто делала то, что требовалось.

```C++
class CSolver {
private:
  ...

public:
  CSolver();

  /* File methods */
  void ReadFile(std::wstring &path);
  void AnalyzeFile(std::wstring &path);
  
  /* Calculations */
  void Preprocessing();
  void Calculate();
  void Work();

  /* Printing the results */
  void PrintResults();
  void PrintResultsShort();

  ...
};
```

Получается, у меня был один большой класс с кучей методов, который выполнял задачу.
Лучше было бы написать следующее.

```C++
class CFile {
private:
  ...

public:
  CFile();

  void ReadFile(std::wstring &path);
  void AnalyzeFile(std::wstring &path);
};

class CPrint {
private:
  ...

public:
  CPrint();

  void PrintResults();
  void PrintResultsShort();
};

class CSolver {
private:
  CFile file;
  CPrint printer;
  ...

public:
  CSolver();

  void Preprocessing();
  void Calculate();
  void Work();

  ...
}
```

 Получается, я бы мог делать все то же самое, но у меня были классы, которые я мог бы переиспользовать в данном проекте (например, если мне просто надо посмотреть файл,
 а не производить над ним какие-то действия).

### Overcomplicating
Я помогал делать курс по Concurrency в этом году. Моя задача была в написании скриптов для создания репозиториев и их дальнейшей настройки.
Во время написания и дальнейшего тестирования я столкнулся с тем, что меня иногда банили, потому что я делал много операций. Мне подсказали решение - exponential backoff.
Я реализовал эту штуку.

```Python
def create_repos(*args, **kwargs):
  flag = 1
  sleep_time = 10

  while flag == 1:
    sleep(sleep_time)
    try:
      CreateRepository(...)
      flag = 0
    catch Exception:
      sleep_time = min(1000, sleep_time * 10)
```

Посмотрев мой код, преподователи курса сказали мне, что для таких retry'ев в Python есть специальный декоратор - @retry. Код стал намного проще.

```Python
@retry(stop_max_attempt_number=5, wait_exponential_multiplier=500)
def create_repos(*args, **kwargs):
  CreateRepository(...)
```
