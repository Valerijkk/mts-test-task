## 1. `README_AUTOTEST.md`

````markdown
# Автотест для поиска AirPods 4 в MTS-Shop

## Структура проекта
project/
├── pages/                   # POM‐классы
│   ├── base_page.py
│   ├── home_page.py
│   └── product_page.py
├── tests/                   # Тесты
│   └── test_airpods4_screenshot.py
├── screenshots/             # Скриншоты страниц
├── reports/                 # HTML-отчёты pytest
├── requirements.txt         # Зависимости, включая webdriver-manager
└── README_AUTOTEST.md       # Этот файл
````

## 1. Установка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/Valerijkk/mts-test-task.git
   cd mts-test-task
   ```
2. Создать и активировать виртуальное окружение:

   ```bash
   python3 -m venv venv
   # Linux/macOS
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```
3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

> **Примечание:** `chromedriver` подхватится автоматически через `webdriver-manager`.

## 2. Запуск

* **Один тест:**

  ```bash
  pytest tests/test_airpods4_screenshot.py -q
  ```
* **Все UI-тесты (маркер `ui`):**

  ```bash
  pytest -m ui -q
  ```
* **С HTML-отчётом:**

  ```bash
  pytest -q --html=reports/report.html --self-contained-html
  ```

## 3. Результаты

* Скриншот сохраняется в `screenshots/`, имя файла выводится в консоль (пример: `screenshots/screenshot_airpods4_page.png`).
* HTML-отчёт — `reports/report.html`.

## Из-за отсутствия доступа к коду сайта, не получилось написать рабочий автотест, тк через код элемента не видны корректные названия элементов, так же из-за множества рекламных всплывающих окон на сайте автотест падал. 
