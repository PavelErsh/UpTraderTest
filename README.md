Тестовое задание Python Developer 

Сделал web приложение которое будет реализовывать древовидное меню,


Дополнительно сделал:
 - написаны тесты
 - всё это помещено в докер контейнер

Для запуска проекта локально:

1 установить зависимости

```pip install -r requirements.txt```


2 запустить проект

```python manage.py runserver```

3 открыть  http://127.0.0.1:8000/

Для запуска через Docker:

1 docker-compose up --build

2 открыть  http://127.0.0.1:8000/

Для запуска тестов локально: python manage.py test menu


Для запуска тестов через docker docker-compose run test