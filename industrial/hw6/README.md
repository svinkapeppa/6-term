# Домашнее задание №6

## Формулировка
Привести примеры антипаттернов в своем коде и исправить их.

### Магическая константа
Одним из заданий в моем проекте было улучшить бота в telegram. Изначально мой код выглядел следующим образом:

```Go
...
bot, err := tgbotapi.NewBotAPI("567524377:AAHfNjID00ESGRJ4vodDA05-gDmmcvY1mYM")
...
```

Затем я заменил его на следующий:

```Go
...
bot, err := tgbotapi.NewBotAPI(os.Getenv("TELEGRAM_TOKEN"))
...
```

Второй вариант предпочтителен не только тем, что не использует никаких непонятных констант, но и что защищает от раскрытия приватного ключа.

### Названия переменных
В этом же проекте была следующая фича: можно было отправлять сообщения с поддержкой форматирования markdown.
Изначально это было реализовано следующим образом:

```Go
...
isMdPtr := flag.Bool("m", false, "Enables Markdown support")
...
send(chatId, text, tgbotapi.NewReplyKeyboard(buttons...), warnl, bot, *isMdPtr)
...
```

Этот код был переписан на следующий:

```Go
...
md := flag.Bool("m", false, "Enables Markdown support")
...
send(chatId, text, tgbotapi.NewReplyKeyboard(buttons...), warnl, bot, *md)
...
```

Второй вариант предпочтительнее, так как флаг используется только как индикатор; не сильно интересует, является ли он указателем.

### Велосипед
Чтобы повторять какое-то действие в Python, если произошла ошибка, не надо писать какие-то свои сложные wrapper'ы.
Есть специальный декоратор @retry со множеством опций.

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

Красиво это выглядит так:

```Python
@retry(stop_max_attempt_number=5, wait_exponential_multiplier=500)
def create_repos(*args, **kwargs):
  CreateRepository(...)
```
