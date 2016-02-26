clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	python manage.py runserver

migrate: clean
	python manage.py migrate

migrations: clean
	python manage.py makemigrations

migrate-auth: clean
	python manage.py migrate authentication

migrations-auth: clean
	python manage.py makemigrations authentication

exclude_migrations: clean
	rm **/migrations/*[0-9]*.py

install:
	pip install -r requirements.txt

user: clean
	python manage.py createsuperuser