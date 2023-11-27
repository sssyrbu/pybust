🐍Pybust: Web content scanner written in Python
===================================================
#### This is an educational project that essentially functions as a web content scanner, searching for existing (and/or hidden) directories on a website. The process involves sending a large number of asynchronous requests to the server and subsequently analyzing the response code. If the code is 200, it means the directory is accessible.
Inspired by [dirb](https://www.kali.org/tools/dirb/#dirb) and [gobuster](https://github.com/OJ/gobuster).

#### Requirements: Python version 3.11 (it won't work on 3.12 due to module compatibility issues with Python 3.12), git, python3-venv, python3-pip.
#### Supported OS: GNU/Linux.

#### Installation: a beginner's guide
Clone the repository:
```
git clone https://github.com/sssyrbu/pybust
```
Navigate to the project directory and initialize the virtual environment:
```
cd pybust
python3 -m venv venv
```
Enter the created virtual environment:
```
source venv/bin/activate
```
Install project dependencies:
```
pip install -r requirements.txt
```
#### Start the script
Navigate to pybuster directory
```
cd pybuster
python3 pybuster.py <endpoints_file> <https://website_link> -o <output_file>
```
Where <endpoints_file> is the file containing the list of endpoints (directories) to be checked. There's already a ready-to-use text file named common.txt in the "wordlists" directory (more wordlists will be added in the future), but you can also use your own file.
<output_file> is the desired name of the result file that will be created.

<output_file> is the desired name of the result file that will be created.

===================================================

#### Это учебный проект, который по сути является сканером веб-контента, который ищет существующие (и/или скрытые) директории веб-сайта. Работа осуществляется за счет отправки большого количества ассинхронных запросов на сервер и последующего анализа кода ответа. Если код равен 200, значит директория доступна.
Вдохновлено утилитами [dirb](https://www.kali.org/tools/dirb/#dirb) и [gobuster](https://github.com/OJ/gobuster)
#### Для работы скрипта потребуются: Python версии 3.11 (на 3.12 пока работать не будет из-за несовместимости модуля aiohttp с Python 3.12), git, python3-venv, python3-pip
#### Поддерживаемые ОС: GNU/Linux

#### Установка: гайд для чайников
Клонируем репозиторий 
```
git clone https://github.com/sssyrbu/pybust
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
Где <endpoints_file> - файл со списком эндпоинтов (директорий) для проверки. В директории wordlists есть готовый текстовый файл common.txt (в дальнейшем wordlists будет дополняться). Но также можно использовать и свой файл.

<output_file> - название файла с результатом, который будет создан.

#### Видео с примером работы
[![Смотреть](https://img.youtube.com/vi/whWOUq_M4zI/default.jpg)](https://www.youtube.com/watch?v=whWOUq_M4zI)
