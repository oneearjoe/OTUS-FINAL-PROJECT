Данный проект является выпускной работой по курсу OTUS Python QA Engineer

# Тема
Frontend-тестирование на основе веб-приложения AutomationExercise и Backend-тестирование на основе API petstore.swagger.io

# Описание
Проект предназначен для автоматизации тестирования:
- **UI-тесты** — реализованы по паттерну PageObject Model (POM).
- **API-тесты** — реализованы через обёртку над библиотекой `requests`.
- Поддерживается запуск локально и в **Selenoid**.
- Поддержка **Allure-отчётов** и логирования (INFO, DEBUG)

## Установка и подготовка окружения
```bash
python -m venv venv
source venv/bin/activate # Linux / MacOS
pip install -r requirements.txt
source env/bin/activate
```
## Пример локального запуска

```bash
pytest -v --browser=chrome --log_level=INFO --alluredir=allure-results
```
## Просмотр результатов в Allure
```bash
allure serve allure-results
```  
Для запуска на selenoid необходимо указать при запуске параметр --selenoid_url и --remote