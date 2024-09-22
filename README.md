# тестовое задание - Парсер решения с сайта https://mathsolver.microsoft.com/ru/solve-problem/x%5E%7B2%7D-3x%2B2%3D0

Проект парсинга решений математических задач
Выполняется парсинг данных со страницы https://mathsolver.microsoft.com/ru/solve-problem/x%5E%7B2%7D-3x%2B2%3D0.Парсер подготавливает данные и сохраняет их в формат json.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=013220)](https://www.python.org/)&nbsp;
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-DC382D.svg?&style=flat&logo=BeautifulSoup&logoColor=white)&nbsp;
![Selenium]<img src=https://img.shields.io/badge/Framework-Selenium-brightgreen>&nbsp;
![Webdriver]<img src=https://img.shields.io/badge/WebDriver-ChromeDriver-blue>&nbsp;


## Оглавление
1. [Описание](#описание)
2. [Стек технологий](##стек-технологий)
3. [Как запустить проект](##как-запустить-проект)
4. [Автор проекта](##автор-проекта)


## Описание проекта:

Парсер, собирающий решение с сайта https://mathsolver.microsoft.com/ru/solve-problem/x%5E%7B2%7D-3x%2B2%3D0
Вся собранная информация сохраняется в файлы с расширением **json**:

## Стек технологий
- Python, BS4, Selenium, WebDriver

## Как запустить проект

Клонировать проект из репозитория
```
git@github.com:vikolga/math_test.git
```

Создать, активировать виртуальное окружение и в него установить зависимости:

```
python -m venv .env
```

```
source .env/Scripts/activate
```

```
pip install -r requirements.txt
```

Запустить парсер из командной строки:

```
python main.py
```

Результатом работы парсера будет создание файла:

```
answers.json
```

## Автор проекта
_[Ольга Викторова](https://github.com/vikolga/)_, python-developer