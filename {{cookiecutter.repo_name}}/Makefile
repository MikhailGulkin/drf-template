up-prod:
	docker-compose -f docker-compose.prod.yaml up --build
down-prod:
	docker-compose -f docker-compose.prod.yaml down -v
update-poetry:
	poetry add $( cat requirements.txt )
install-hooks:
	pre-commit install -t pre-commit
