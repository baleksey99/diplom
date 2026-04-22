# Личный дневник (Personal Diary)

Веб-приложение для ведения личного дневника с возможностью создавать, редактировать, удалять и искать записи.

## 📋 Функциональность

- Регистрация и аутентификация пользователей
- Создание новых записей
- Просмотр списка всех записей
- Просмотр отдельных записей
- Редактирование записей
- Удаление записей
- Поиск по заголовку и содержимому записей
- Адаптивный дизайн на Bootstrap 5

## 🛠 Технологии

- Python 3.14
- Django 4.2.30
- PostgreSQL
- Bootstrap 5
- HTML5/CSS3

## 📁 Структура проекта
diplom/
├── diary/ # Основное приложение
│ ├── migrations/ # Миграции базы данных
│ ├── templates/
│ │ └── diary/ # Шаблоны приложения
│ │ ├── entry_list.html
│ │ ├── view_entry.html
│ │ ├── create_entry.html
│ │ ├── edit_entry.html
│ │ ├── delete_entry.html
│ │ ├── search_results.html
│ │ └── success.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py # Формы для записей
│ ├── models.py # Модель Entry
│ ├── urls.py # URL-маршруты приложения
│ └── views.py # View-функции
├── diary_project/ # Проект Django
│ ├── init.py
│ ├── settings.py # Настройки проекта
│ ├── urls.py # Корневые URL-маршруты
│ └── wsgi.py
├── templates/ # Глобальные шаблоны
│ ├── base.html # Базовый шаблон
│ └── registration/
│ ├── login.html # Шаблон входа
│ └── register.html # Шаблон регистрации
├── static/ # Статические файлы
├── manage.py # Управляющий скрипт Django
└── README.md # Документация

text

## 🚀 Установка и запуск

### 1. Клонирование репозитория

bash
git clone <repository-url>
cd diplom
2. Создание виртуального окружения
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей
bash
pip install django psycopg2-binary
4. Настройка базы данных PostgreSQL
Создайте базу данных и пользователя:

sql
CREATE DATABASE diplom_db;
CREATE USER baleksey99 WITH PASSWORD 'baleksey99';
ALTER ROLE baleksey99 SET client_encoding TO 'utf8';
ALTER ROLE baleksey99 SET default_transaction_isolation TO 'read committed';
ALTER ROLE baleksey99 SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE diplom_db TO baleksey99;
5. Применение миграций
bash
python manage.py makemigrations
python manage.py migrate
6. Создание суперпользователя (опционально)
bash
python manage.py createsuperuser
7. Запуск сервера разработки
bash
python manage.py runserver
Приложение будет доступно по адресу: http://127.0.0.1:8000/

# Использование
## Регистрация
Перейдите на страницу регистрации

Введите имя пользователя и пароль

Нажмите "Зарегистрироваться"

## Вход в систему
Перейдите на страницу входа

Введите имя пользователя и пароль

Нажмите "Войти"

Работа с записями
Создание записи: Нажмите "Новая запись", заполните заголовок и содержание

Просмотр записи: Нажмите "Читать" на карточке записи

Редактирование: Нажмите "Редактировать" на карточке или странице просмотра

Удаление: Нажмите "Удалить" и подтвердите действие

Поиск: Используйте поисковую строку для поиска по заголовкам и содержимому

# Конфигурация
Основные настройки (settings.py)
python
# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diplom_db',
        'USER': 'baleksey99',
        'PASSWORD': 'baleksey99',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# URL-редиректы
LOGIN_REDIRECT_URL = 'diary:entry_list'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    }
]
# Модель данных
## Entry (Запись)
Поле	Тип	Описание
title	CharField(max_length=200)	Заголовок записи
content	TextField	Содержание записи
author	ForeignKey(User)	Автор записи
created_at	DateTimeField(auto_now_add=True)	Дата создания
updated_at	DateTimeField(auto_now=True)	Дата обновления
## URL-маршруты
Корневые маршруты
URL	Имя	Описание
/register/	register	Регистрация
/login/	login	Вход
/logout/	logout	Выход
/admin/	admin	Админ-панель
## Маршруты приложения diary (пространство имен: diary)
URL	Имя	Описание
/	entry_list	Список записей
/search/	search_entries	Поиск записей
/create/	create_entry	Создание записи
/<int:pk>/	view_entry	Просмотр записи
/<int:pk>/edit/	edit_entry	Редактирование
/<int:pk>/delete/	delete_entry	Удаление
# Используемые технологии фронтенда
Bootstrap 5.3.0 - CSS-фреймворк

CDN подключение для быстрой загрузки

# Безопасность
CSRF-защита для всех форм

Требование аутентификации для доступа к записям (декоратор @login_required)

Защита от несанкционированного доступа к чужим записям

Пароли хэшируются с использованием алгоритмов Django по умолчанию

# Возможные проблемы и решения
Ошибка "NoReverseMatch"
Убедитесь, что во всех шаблонах используется правильное пространство имен:

Для маршрутов приложения: {% url 'diary:entry_list' %}

Для маршрутов аутентификации: {% url 'login' %}

Ошибка CSRF
Убедитесь, что в каждой POST-форме есть тег {% csrf_token %}

Проблемы с подключением к PostgreSQL
Проверьте:

Запущен ли сервер PostgreSQL

Правильность учетных данных в settings.py

Существует ли база данных

# Зависимости
text
Django==4.2.30
psycopg2-binary==2.9.9
👨‍# Разработчик
Имя: baleksey99

Email: baleksey99@example.com

# Лицензия
Этот проект создан в учебных целях.

# Вклад в проект
Форкните репозиторий

Создайте ветку для новой функции (git checkout -b feature/amazing-feature)

Зафиксируйте изменения (git commit -m 'Add amazing feature')

Отправьте изменения в ветку (git push origin feature/amazing-feature)

Откройте Pull Request

# Поддержка
При возникновении вопросов или проблем создайте Issue в репозитории проекта.

Приятного использования! 📔✨