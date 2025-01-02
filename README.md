# HelloWorldOnSteroids


Это забавный тренировочный проект, направленный на демонстрирование возможностей работы с консолью с помощью Python.\
В этом проекте были затронуты такие возможности форматирования ввода/вывода в консоль, как:
- Вывод цветного текста
- Перезаписывание содержимого
- Имитация движения текста

## Важно
Для нормальной работы программы необходимо использовать стандартную системную консоль.\
Встроенные в IDE консоли (например, run в PyCharm) не подойдут для корректной работы.\
Поэтому внимательно следуйте инструкции по установке и запуску.

## Инструкция по установке и запуску в терминале
Данная инструкция будет ориентирована на пользователей Windows. Для пользователей Unix-систем общий принцип работы будет такой же, но отличительные черты мы приводить здесь не будем.
1. Перейдите в каталог, в который хотите установить проект.
2. Инициируйте Git репозиторий:
```commandline
git init
```
3. Далее клонируйте репозиторий:
```commandline
git clone https://github.com/Lofienjoyerr/HelloWorldOnSteroids
```
4. Убедитесь, что у вас установлен Python на компьютер. Для этого можно использовать команду:
```commandline
python --version
```
5. Создайте виртуальное окружение:
```commandline
python -m venv .venv
```
6. Активируйте виртуальное окружение.\
Для cmd используйте:
```commandline
.venv\Scripts\activate
```
Для powershell убедитесь, что у вас разрешён запуск сценариев. Затем используйте:
```commandline
.venv\Scripts\activate.ps1
```
7. Скачайте все необходимые библиотеки:
```commandline
pip install -r HelloWorldOnSteroids\requirements.txt
```
8. Перейдите в корневую папку проекта:
```commandline
cd HelloWorldOnSteroids
```
9. Запустите файл main.py:
```commandline
python main.py
```

## Инструкция по установке и запуску в PyCharm
1. Запустите IDE и создайте проект в интересующей вас директории. При создании проекта также создайте виртуальное окружение.
2. Инициируйте Git репозиторий:
```commandline
git init
```
3. Далее клонируйте репозиторий:
```commandline
git clone https://github.com/Lofienjoyerr/HelloWorldOnSteroids
```
4. Убедитесь, что у вас установлен Python на компьютер. Для этого можно использовать команду:
```commandline
python --version
```
5. Создайте виртуальное окружение:
```commandline
python -m venv .venv
```
6. Активируйте виртуальное окружение.\
Для cmd используйте:
```commandline
.venv\Scripts\activate
```
Для powershell убедитесь, что у вас разрешён запуск сценариев. Затем используйте:
```commandline
.venv\Scripts\activate.ps1
```
7. Запустите файл main.py:
```commandline
python HelloWorldOnSteroids\main.py
```