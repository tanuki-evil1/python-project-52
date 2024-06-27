build:
	./build.sh

install:
	poetry install

start:
	poetry run gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate