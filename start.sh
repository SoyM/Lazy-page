docker build -t soym/django-app .
docker run --name red \
-v /usr/src \
-v /usr/src/static \
-p 12000:8000 \
-d soym/django-app /usr/local/bin/uwsgi --http :8000 --chdir /usr/src -w red.wsgi