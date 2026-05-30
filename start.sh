python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn virtual_env.wsgi:application --bind 0.0.0.0:$PORT