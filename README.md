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

## Развертывание на виртуальной машине

Проверялось на Ubuntu 24.04. Порт приложения - 5000.

```bash
# 1. Установить нужные пакеты
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv

# 2. Склонировать репозиторий
git clone https://github.com/Nepreff/cloud-project.git
cd cloud-project

# 3. Создать виртуальное окружение и поставить зависимости
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Задать настройки (необязательно)
export APP_NAME="Cloud project on VM"

# 5. Запустить
python app.py
```

Проверка из второй консоли:

```bash
ss -ltnp | grep 5000
curl http://127.0.0.1:5000
```

Для доступа с хоста нужно открыть порт 5000 (при NAT - сделать проброс порта) и зайти на `http://IP_ВМ:5000`.

Обновление кода:

```bash
git status
git pull
```
