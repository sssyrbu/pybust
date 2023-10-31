🐍Pybust: Web content scanner written in Python
===================================================
Это учебный проект, который по сути является сканером веб-контента, который ищет существующие (и/или скрытые) директории веб-сайта. Работа осуществляется за счет отправки большого количества ассинхронных запросов на сервер и последующего анализа кода ответа. Если код равен 200, значит директория доступна.
Вдохновлено утилитами [dirb](https://www.kali.org/tools/dirb/#dirb) и [gobuster](https://github.com/OJ/gobuster)
### Для работы скрипта потребуются: Python версии 3.11 (на 3.12 пока работать не будет из-за несовместимости модуля aiohttp с Python 3.12), git, python3-venv, python3-pip
### Поддерживаемые ОС: GNU/Linux

#### Установка: гайд для чайников
Клонируем репозиторий 
```
git clone git@github.com:sssyrbu/pybust.git
```
Переходим в директорию проекта и инициализируем виртуальное окружение
```
cd pybust
python3 -m venv venv
```
Заходим в созданное ранее виртуальное окружение
```
source venv/bin/activate
```
Устанавливаем зависимости проекта
```
pip install -r requirements.txt
```
#### Запуск скрипта
Для запуска скрипта нам понадобиться перейти в директорию pybuster
```
cd pybuster
python3 pybuster.py <endpoints_file> <https://website_link> -o <output_file>
```
Где <endpoints_file> - файл со списком эндпоинтов (директорий) для проверки. Файл должен быть в директории **pybuster**. Пример такого файла: https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt
<output_file> - название файла с результатом, который будет создан.

#### Видео с примером работы (нажать на картинку)
[![Смотреть](https://img.youtube.com/vi/whWOUq_M4zI/default.jpg)](https://www.youtube.com/watch?v=whWOUq_M4zI)
