# cloud-project

Учебный проект по дисциплине «Основы облачных технологий».

## Запуск в Docker

Сборка образа:

```bash
docker build -t cloud-project:v1 .
```

Запуск контейнера (порт 5000 в контейнере пробрасывается на порт 8080 на хосте):

```bash
docker run -d --name cloud-app -p 8080:5000 cloud-project:v1
```

Проверка:

```bash
docker ps
docker logs cloud-app
curl http://localhost:8080
```

Должна вывестись строка `Cloud project is running in Docker!`

Можно поменять название приложения через переменную окружения:

```bash
docker run -d --name cloud-app-env -p 8081:5000 -e APP_NAME="My Docker App" cloud-project:v1
```

Остановка и запуск:

```bash
docker stop cloud-app
docker start cloud-app
```
