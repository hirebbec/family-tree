# family-tree
# Настройка и управление проектом на Python (Windows)

## Виртуальное окружение
1. Создание виртуального окружения:
	```bash
	python -m venv venv
	```
2. Активация виртуального окружения:
	```bash
	.\venv\Scripts\activate
	```
3. Деактивация виртуального окружения:
	```bash
	deactivate
	```

## Управление пакетами с помощью pip
1. Установка пакета:
	```bash
  	pip install <package>
	```
2. Установка пакетов из requirements.txt:
	```bash
	pip install -r requirements.txt
	```
 
## Poetry
1. Инициализация нового проекта:
	```bash
  	poetry init
	```
2. Установка зависимостей:
	```bash
	poetry install
	```
3. Добавление новой зависимости:
	```bash
	poetry add <package>
	```
4. Активация виртуального окружения Poetry:
   ```bash
   poetry shell
   ```
5. Блокировка зависимостей в poetry.lock:
   ```bash
   poetry lock
   ```

## Alembic
1. Инициализация Alembic:
	```bash
  	alembic init db/migrations
	```
2. Создание новой миграции:
	```bash
	alembic revision --autogenerate -m "описание миграции"
	```
3. Применение миграций:
	```bash
	alembic upgrade head
	```
 
## Git
1. Инициализация репозитория:
	```bash
  	git init
	```
2. Добавление изменений:
	```bash
	git add .
	```
3. Коммит изменений:
	```bash
	git commit -m "описание изменений"
	```
4. Отправка изменений на удаленный репозиторий:
   ```bash
   git push
   ```
5. Клонирование репозитория:
	```bash
	git clone <repository_url>
	```
 
## Mypy
1. Проверка типов в проекте:
	```bash
  	mypy .
	```
 
## Ruff 
1. Проверка проекта на наличие ошибок:
	```bash
  	ruff .
	```
2. Автоисправление ошибок:
	```bash
	ruff . --fix
	```

## Docker Compose
1. Пересборка сервисов после изменения конфигурации:
	```bash
  	docker-compose up --build
	```
2. Запуск сервисов с помощью docker-compose:
	```bash
	docker-compose up
	```

## Docker
1. Просмотр всех образов Docker:
	```bash
  	docker images
	```
2. Посмотреть логи контейнера:
	```bash
	docker logs <container_id>
	```
3. Вход в работающий контейнер:
	```bash
	docker exec -it <container_id> /bin/bash
	```
4. Просмотр работающих контейнеров:
   ```bash
   docker ps
   ```
5. Сборка Docker-образа:
	```bash
	docker build -t <image_name> .
	```
6. Запуск контейнера:
   ```bash
   docker run -d -p <host_port>:<container_port> <image_name>
   ```