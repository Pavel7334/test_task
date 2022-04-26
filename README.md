# test_task

Запуск проекта.
 - Скопировать проект с помощью ``` git clone https://github.com/iNgredie/Simbirsoft_spring_practicum.git ```
 - ```docker-compose up --build ```  собрать приложение и сделать его первоначальный запуск
 - ```docker-compose down -v``` – остановить работу приложения
 - ```docker-compose run web python manage.py migrate``` – сделать необходимые миграции
 - ```docker-compose run web python manage.py loaddata fixtures.json``` – что бы применить фикстуры
 - ```docker-compose up``` – окончательно запустить приложение.
 
 
Ссылки на эндпоинты
- ```http://localhost:8000/api/article/``` - получение всех статей
- ```http://localhost:8000/api/article/<int:pk>``` - получение одной статьи
- ```http://localhost:8000/api/comment/``` - получение всех комментариев
- ```http://localhost:8000/api/comment/<int:pk>``` - получить все вложенные комментарии комментария

Стек технологий и требований к ним для реализации веб-приложения 

- Python 3
- Django 
- Django REST framework
- СУБД PostgreSQL (через отдельный Docker-образ)
- Контейнер с приложением должен использовать alpine
- Описание API - Swagger OpenAPI Version 3

---
- Swagger достпупен по ссылке: ```http://localhost:8000/swagger```
