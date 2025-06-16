
# GitSync Hub

A Django app that asynchronously clones GitHub repositories and stores their JSON metadata in a PostgreSQL database using Celery.

## 🚀 Features

- Clone public GitHub repositories using their URL
- Parse and store metadata as structured JSON
- Asynchronous task handling with Celery
- Persistent storage in PostgreSQL
- Easily extendable for analytics, syncing intervals, or GitHub webhooks

## 🔧 Tech Stack

- Django
- Celery
- PostgreSQL
- GitHub API
- Docker (optional for containerization)

## 📦 Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/egenius01/GitSyncHub.git
cd GitSyncHub
```

2. Create a virtual environment and activate it.

3. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the server:
```bash
python manage.py runserver
```

6. Start Celery worker:
```bash
celery -A project_name worker --loglevel=info
```

## 📸 Screenshots

![gitsync1](https://user-images.githubusercontent.com/32688387/225042349-a17778ad-e7a7-4076-91f1-8670965c00f5.png)
![gitsync-1](https://user-images.githubusercontent.com/32688387/225042410-25a0c307-bdb1-495d-a2c5-081ba2aa6f7b.png)
![gitsync2](https://user-images.githubusercontent.com/32688387/225042537-9a6e89b6-5afa-411b-9143-abddf90deaab.png)
![gitsync3](https://user-images.githubusercontent.com/32688387/225042553-a88ad31f-1fe3-4c3c-bead-307ecb189f2e.png)
![gitsync4](https://user-images.githubusercontent.com/32688387/225042554-14ece648-adc8-4d3e-ae7f-1ebb4fe94f06.png)

## 📘 Documentation

- [Celery Setup Guide](docs/celery.md)
- [API Reference](docs/api.md)
- [Architecture Diagram](docs/architecture.png)

## ✅ Roadmap

- Add periodic sync with Celery Beat
- Webhook support from GitHub
- Frontend dashboard for repo insights

## 👤 Author

- [@egenius01](https://github.com/egenius01)

