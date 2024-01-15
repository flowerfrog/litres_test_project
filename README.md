<h1> Проект по тестированию сервиса электронных и аудиокниг "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](design/image/litres_page.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Удаление книги из корзины
- [x] Добавление книги в Избранное
- [x] Удаление книги из Избранного

### API-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину

### Mobile-тесты
- [x] Поиск книги(успешный и неуспешный)
- [x] Добавление книги в Сохраненное
- [x] Удаление книги из Сохраненного

----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/LitresTestProject/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

* `comment` - комментарий


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/LitresTestProject/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать браузер
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure отчет


#### Общие результаты
![This is an image](design/image/allure_report_overview.png)
#### Список тест кейсов
![This is an image](design/image/allure_report.png)
#### Пример отчета о прохождении ui-теста
![This is an image](design/image/example_test_ui_allure.png)
#### Пример отчета о прохождении api-теста
![This is an image](design/image/example_test_api_allure.png)
#### Пример отчета о прохождении mobile-теста
![This is an image](design/image/example_test_mobile_allure.png)

----
### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3942/dashboards">Ссылка на проект в AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Тест-планы проекта
![This is an image](design/image/allure_TestOps_test_plans.png)

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](design/image/allure_TestOps_test_cases.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](design/image/example_autotests_allure_TestOps.png)

#### Тестовые артефакты
![This is an image](design/image/allure_TestOps_attachment.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](design/image/allure_TestOps_dashboard.png)

#### История запуска тестовых наборов
![This is an image](design/image/allure_TestOps_launches.png)

----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1045">Ссылка на проект в Jira</a>

![This is an image](design/image/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](design/image/tg_notification.png)

----
### Пример видео прохождения ui-автотеста
![autotest_gif](design/image/autotest.gif)

### Пример видео прохождения mobile-автотеста
![autotest_gif](design/image/autotest_mobile.gif)
