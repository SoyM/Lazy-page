# Lazy-page

A web application for [foolbot](https://github.com/SoyM/foolbot) and [esp32bot](https://github.com/SoyM/Esp32bot)

## Usage
* Install docker and docker-compose
* run `docker-compose up`

## Database

```bash
python manage.py makemigrations red

python manage.py migrate

python manage.py loaddata red_data.json
```
### create your superuser

```bash
python manage.py createsuperuser
```
