# Приложение QRKot

### Описание
Сервис сбора пожертвований на различные целевые проекты для поддержки котиков.

**Проекты**  
У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.

**Пожертвования**  
Пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

**Пользователи**  
- Целевые проекты создаются администраторами сайта.
- Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
- Любой пользователь может видеть список всех проектов.

Примеры запросов к API, варианты ответов и ошибок приведены в документации проекта, доступной по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Технологии
- Python 3.8.9
- FastAPI 0.78.0

### Шаблон наполнения файла `cat_charity_fund/.env`
```
APP_TITLE=Приложение QRKot
APP_DESCRIPTION=Сервис сбора пожертвований для поддержки котиков.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secret
```

### Запуск проекта
- Клонируйте репозиторий и перейдите в папку проекта:
```
git clone https://github.com/marusya-zh/cat_charity_fund.git
```
```
cd cat_charity_fund
```
- Установите и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
- Запустите проект командой:
```
uvicorn app.main:app
```

### Автор
Mariya Zhuchina