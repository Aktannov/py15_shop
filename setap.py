# 1) создать дерикторию для проектов


# 2) в этой директории необходимо создать виртуальное окружение - pynthon3 -m venv name, активировать его - source название_окружения/bin/activate

# 3) в папке проекта необходимо создать папку зависимости requirements.txt и опсиать все библиотеки, которые будут использованы в проекте

# 4) установить все зависимости в виртуальное окружение
# pip install -r requirements.txt
# Django
# psycopg2-binary
# djangorestframework
# django-filter
# python-decouple
# Pillow
# drf-yasg



# 5) создаем Django проект: django-admin starproject название_проекта .

# 6) создаем приложение проекта
# ./manage.py startapp название

# 7) создаем базу данных для проекта
# psql -> CREATE DATABASE name;

# 8) настройка проекта
# указываем приложения в INSTALLED_APPS
# указываем настройки БД
# указываем еастройки языка, часового пояса

# 9)создаем модель пользователя
# в settings добовляем настройку AUTH_USER_MODEL

# 10) определяем остольные модели

# 11) делаем миграции
# ./manage.py makemigrations
# ./manage.py migrate

# 12) создать админа
# ./manage.py createsuperuser
