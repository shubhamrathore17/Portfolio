web: gunicorn portfolio.wsgi:application --log-file -
python manage.py makemigrations
release: python manage.py migrate
python manage.py collectstatic
