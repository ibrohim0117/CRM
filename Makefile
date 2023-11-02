mig:
	python manage.py makemigrations app
	python manage.py migrate app

run:
	python manage.py runserver
