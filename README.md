# Кейс 1. Автодеплой: GitHub Actions, Docker и GitFlow

Простой Flask-сервис, демонстрирующий автодеплой через GitHub Actions:

1. `push` в ветку `main` запускает workflow `.github/workflows/deploy.yml`;
2. workflow собирает Docker-образ и пушит его в GitHub Container Registry (GHCR);
3. отдельный job деплоит образ на сервер через SSH (appleboy/ssh-action).

## Локальный запуск

```bash
pip install -r requirements.txt
python app.py
# http://localhost:8000/health
```

## Docker

```bash
docker build -t flask-autodeploy-case .
docker run -p 8000:8000 flask-autodeploy-case
```

## GitFlow

- фичи — в ветках `feature/*`;
- релизы — через PR в `main`;
- деплой срабатывает только на `push` в `main`.

## Секреты для SSH-деплоя

В Settings → Secrets and variables → Actions добавить:

- `SSH_HOST` — адрес сервера;
- `SSH_USERNAME` — пользователь;
- `SSH_KEY` — приватный ключ;
- (опционально) `SSH_PORT` — по умолчанию 22.
