# absolutions

Автотесты для проекта "absolutions"

#### Стэк
- язык программирования - [Python 3.10](https://www.python.org/downloads/)
- тестовый фреймворк - [pytest](https://docs.pytest.org/en/latest/)
- ui-автоматизация: [Selenium](https://selenium-python.readthedocs.io/index.html), [Selene](https://github.com/yashaka/selene)
- отчеты - [allure](https://docs.qameta.io/allure/)

#### Структура
```bash
.
├── core
│   ├── common              # общий модуль для всех проектов
│   ├── data                # тестовые данные, дата-билдеры  
│   ├── pages               # описание классов страниц (PageObjects)
│   ├── service             # сервисные скрипты (ручной запуск, подготовка среды)
│   ├── utils               # утилиты и хелперы текущего проекта
├── tests
│   ├── test_suite_name.py  # тесты 
│   ├── conftest.py         # фикстуры
│   └── pytest.ini          # конфигурация pytest
├── .gitignore              # список игнорируемых гитом файлов, папок    
├── config.yaml             # параметры конфигурации проекта
└── requirements.txt        # подключение внешних библиотек
└── settings.py             # класс для работы с параметрами конфигурации проекта
```

## Установка
1. Клонируем проект
   <br>`git clone https://github.com/alpikin63/absolutins.git`
2. В проекте устанавливаем виртуальное окружение [virtualenv](https://virtualenv.pypa.io/en/latest/) и активируем его:
<br> Windows `venv\Scripts\activate.bat`
<br> MacOS/Linux `source venv/bin/activate`
<br> PyCharm - следуем подсказкам или через настройки добавляем интерпретатор
3. Устанавливаем все зависимости из файла `requirements.txt`
<br> `pip install -r requirements.txt`
4. Скачать пакет [allure](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.9.0/allure-commandline-2.9.0.zip). Архив распаковать в каталоге проекта в отдельной папке: ./allure-cli

## Запуск
- для regress тестирования::
<br>`py.test -v -l -m "regress" --alluredir=allure-results .\tests\ui\`

## Сформировать отчет:
Выполнить команду:
<br>`\allure-cli\bin\allure serve .\allure-results`
