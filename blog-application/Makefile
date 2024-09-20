dev:
	python manage.py runserver --settings=config.settings.dev

kevin-dev:
	python manage.py runserver --settings=config.settings.dev_kevin

prod:
	python manage.py runserver --settings=config.settings.prod

dev-shell:
	python manage.py shell --settings=config.settings.dev

prod-shell:
	python manage.py shell --settings=config.settings.prod

dev-install:
	pip3 install -r requirements/dev.txt

prod-install:
	pip3 install -r requirements/prod.txt

migrate:
	python manage.py migrate --settings=config.settings.prod

dev-migrate:
	python manage.py migrate --settings=config.settings.dev
	
prod-migrate:
	python manage.py migrate --settings=config.settings.prod
dev-makemigration:
	python manage.py makemigrations $(m) --settings=config.settings.dev

prod-makemigration:
	python manage.py makemigrations $(m) --settings=config.settings.prod

dev-invest:
	python manage.py sqlmigrate $(m) $(i) --settings=config.settings.dev

dev-cs:
	python manage.py collectstatic --settings=config.settings.dev