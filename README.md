D6 Проект: Приют домашних животных


Для проверки задания локально:

1. Создать новый катог виртуального окружения

python -m venv <Имя каталога>

2. Стянуть репозиторий к себе, скопировать каталог animal_shelter в каталог виртуального окружения.

3. Активировать виртуальное окружение.

4. Перейти в каталог проекта:

cd animal_shelter

5. Установить зависимости из requirements.txt:

pip install -r requirements.txt

6. Выполнить миграции для создания БД:

python manage.py makemigrations

python manage.py migrate

7. Импортировать в БД данные:

python manage.py loaddata data.xml

8. Запустить сервер:

python manage.py runserver

9. Открыть URL:

http://127.0.0.1:8000/


P.S. Для входа в "админку" не забудьте сгенерировать себе логин/пароль:

python manage.py createsuperuser
