run:
	docker-compose build
	docker-compose up -d

format:
	black Api/
	isort Api/
