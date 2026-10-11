#!/bin/bash
set -e

echo "Starting deployment..."

git pull origin main

source venv/bin/activate

pip install -r requirements.txt

alembic upgrade head

sudo systemctl restart fastapi-blog

echo "Deployment completed successfully!"