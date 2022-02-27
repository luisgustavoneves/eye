# The Eye

## To run the main application
python manage.py runserver

## To run celery task
celery -A eye worker --loglevel=info