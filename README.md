Обрезка ссылок с помощью Bitly
========================
Принимает на вход ссылку. Выводит обрезанную ссылку. Если ссылка введена с ошибкой, выводит сообщение:"Вы ввели неправильную ссылку". Если введена уже обрезанная ссылка, выводит сообщение с количеством кликов по введенной ссылке.

Как установить
-------------------------
Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

Получение токена
-------------------------
Для корректной работы программы необходио иметь персональный токен `BITLY_TOKEN`. Для его получения, зарегистриуйтесь на [bitly.com](https://bitly.com/a/sign_up). В разделе "Profile Settings" нажмите "Generic Access Token".

Пример работы
-------------------------
```
$ python main.py https://dvmn.org/
https://bit.ly/2P4hRWf

$ python main.py https://bit.ly/2P4hRWf
Общее количество кликов : 0
```

Цель проекта
-------------------------
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
