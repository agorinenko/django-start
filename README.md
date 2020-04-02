# Стартовый шаблон проекта для Django
Python	    ``3.7``<br/>
Django	    ``3.0.5``<br/>
DRF	        ``3.11.0``<br/>
Channels	``2.4.0``<br/>
Postgres    ``12``
## Первый запуск

### Env
Создать .env файл
``` bash
cp .env.example .env
```
### Запуск контейнеров postgres и redis
``` bash
docker-compose up -d
```

### Pip
Установка зависимостей
``` bash
pip install -r requirements.txt
```

### Добавить лог-файл
```bash
mkdir logs
```

### Миграции
Создание, если нужно
``` bash
python manage.py makemigrations
```
Накатываем
``` bash
python manage.py migrate
```

### Создание администратора
``` bash
python manage.py createsuperuser
```
## Для работы
### Миграции
Создание, если нужно
``` bash
python manage.py makemigrations
```
Накатываем
``` bash
python manage.py migrate
```
Просмотр миграций
``` bash
python manage.py showmigrations
```
Откатываем все миграции приложения
``` bash
python manage.py migrate app_name zero
```
или возвращаемся к 0001_initial
``` bash
python manage.py migrate app_name 0001_initial
```
Загрузка тестовых данных
``` bash
python manage.py loaddata apps/{{app_name}}/data/init_01.json
python manage.py dumpdata apps.Office --output apps/{{app_name}}/data/init_01.json
```
Создание пустой миграции
``` bash
python manage.py makemigrations --empty app_name
```
### Создание приложения
``` bash
python manage.py startapp app_name
```
### Запуск тестов из консоли
``` bash
python manage.py test --verbosity=3
```