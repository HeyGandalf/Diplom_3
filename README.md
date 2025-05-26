
# UI Автотесты для Stellar Burgers

Этот проект содержит автоматизированные UI-тесты для веб-приложения [Stellar Burgers](https://stellarburgers.nomoreparties.site/), реализованные с использованием `pytest`, `selenium`, `allure` и паттерна Page Object Model.

## 🧰 Стек технологий

- Python 3.9+
- pytest
- selenium
- allure-pytest
- faker

## 🚀 Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/your_username/stellar-burgers-tests.git
   cd stellar-burgers-tests
   ```

2. Создай виртуальное окружение и активируй его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # для Mac/Linux
   venv\Scripts\activate     # для Windows
   ```

3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## ✅ Запуск тестов

Запуск всех тестов:
```bash
pytest
```

Запуск с Allure:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

Запуск только одного теста:
```bash
pytest tests/test_account.py::test_log_out
```

## 🧪 Покрытие тестами

- Вход в аккаунт
- Переходы между страницами
- Восстановление пароля
- Личный кабинет
- Оформление заказа
- Интеракции с ингредиентами

## 📝 Автор

Автотесты написаны Женей (PyFinders).
