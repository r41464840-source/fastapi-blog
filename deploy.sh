#!/bin/bash
set -e

echo "Starting deployment..."

cd /home/ubuntu/fastapi-blog

if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "ERROR: Local changes detected. Deployment stopped to protect them."
    git status --short
    exit 1
fi

git pull --ff-only origin main

source venv/bin/activate

pip install -r requirements.txt

alembic upgrade head

sudo systemctl restart fastapi-blog

sudo systemctl is-active --quiet fastapi-blog

echo "Deployment completed successfully!"
