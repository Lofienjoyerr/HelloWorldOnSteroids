# HelloWorldOnSteroids


Это забавный тренировочный проект, направленный на демонстрирование возможностей работы с консолью с помощью Python.\
В этом проекте были затронуты такие возможности форматирования ввода/вывода в консоль, как:
- Вывод цветного текста
- Перезаписывание содержимого
- Имитация движения текста

## Важно
Для нормальной работы программы необходимо использовать стандартную системную консоль.\
Встроенные в IDE консоли (например, run в PyCharm) не подойдут для корректной работы.\
Следующие инструкции будут ориентированы на пользователей Windows. Для пользователей Unix-систем общий принцип работы будет такой же, однако отличительные черты мы приводить здесь не будем.\
Поэтому внимательно следуйте инструкциям по установке и запуску.

## Инструкция по установке и запуску в терминале
1. Перейдите в каталог, в который хотите добавить проект.
2. Далее клонируйте репозиторий:
```commandline
git clone https://github.com/Lofienjoyerr/HelloWorldOnSteroids
```
3. Перейдите в корневую папку проекта:
```commandline
cd HelloWorldOnSteroids
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
pip install -r requirements.txt
```
8. Запустите файл main.py:
```commandline
python main.py
```

## Инструкция по установке и запуску в PyCharm
1. Запустите IDE и откройте директорию, в которую хотите установить проект.
2. Далее откройте терминал и клонируйте репозиторий:
```commandline
git clone https://github.com/Lofienjoyerr/HelloWorldOnSteroids
```
3. Перейдите в корневую папку проекта:
```commandline
cd .\HelloWorldOnSteroids\
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
.\.venv\Scripts\activate
```
7. Скачайте все необходимые библиотеки:
```commandline
pip install -r .\requirements.txt
```
8. Зайдите в настройки Run -> Edit configurations -> Edit configuration templates, слева выберите python и включите опцию emulate terminal in output console. В зависимости от версии PyCharm данная настройка будет находиться либо внизу окна конфигурации, либо справа сверху в Modify options.
9. Запустите файл main.py с помощью средств IDE или терминала.\
Команда для терминала внутри IDE:
```commandline
python .\main.py 
```