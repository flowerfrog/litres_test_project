<h1> Проект по тестированию сервиса электронных и аудиокниг "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](design/image/litres_page.png)

<u><h3> Список проверок, реализованных в автотестах:</h3></u>

>### UI-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину
- [x] Удаление книги из корзины
- [x] Добавление книги в Избранное
- [x] Удаление книги из Избранного

>### API-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги
- [x] Добавление книги в корзину

----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenium.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----
### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/LitresTestProject/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

* `browser` - параметр определяет браузер для запуска тестов

* `comment` - комментарий


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/LitresTestProject/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать браузер
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](design/image/jenkins_build.png)

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

----