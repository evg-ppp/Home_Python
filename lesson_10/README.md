# Lesson 10

## Описание проекта

Автоматизированные UI-тесты, выполненные с использованием:

- Python
- Pytest
- Selenium WebDriver
- Page Object
- Allure Report

Проект содержит тесты:
- проверки калькулятора;
- оформления заказа в интернет-магазине Saucedemo.

---

## Запуск тестов

```bash
pytest
```

Команда запускает все тесты проекта.

---

## Формирование результатов Allure

```bash
pytest --alluredir=allure-results
```

После выполнения создается папка **allure-results**, содержащая результаты тестирования.

---

## Просмотр отчета Allure

```bash
allure serve allure-results
```

Если команда `allure` не добавлена в переменную среды **PATH**, можно использовать полный путь:

```bash
C:\Tools\allure\bin\allure.bat serve allure-results
```

---

## Проверка стиля кода

```bash
flake8 .
```

Команда проверяет код на соответствие стандарту **PEP 8**.
