# Итоговый проект курса "Работа с внешними API"  

REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке.

# Проект YaMDb  
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title).<br>  
Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список категорий (Category) может быть расширен.<br>  
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.<br>  
В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр из списка предустановленных.<br>  
Новые жанры может создавать только администратор.<br>  
Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и выставляют произведению рейтинг.<br>  
## Используемые технологии:
>- Python 3.10 
>- Aiogram 2.23.1

  
## Установка<br>  

Для работы приложения требуется установка на ваш компьютер **[Python](https://www.python.org/downloads/)**, **[Docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows)**, **[Docker-Compose](https://docs.docker.com/compose/install/)**.

***Склонируйте репозиторий***:
``` bash
git clone git@github.com:KAbashin/infra_sp2.git
```
***Запустите docker-compose:***:
``` bash
docker-compose up -d
``` 


## Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

***Скачать образ YaMDb из репозитория на DockerHub:***
```bash
docker pull kabashin/infra_sp2:v3
```



Разработчик:<br>
Ярослав Абашин <br>E-mail: kabashin@mail.ru<br>Telegram @qpwofk<br>
