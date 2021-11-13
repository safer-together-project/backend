#!/bin/bash

echo "Deploy script start (deploy.sh)"
echo "Fetching latest repo..."

cd /home/deploy/steds-care-backend/

git pull

echo "\n\nUpdate Python Dependencies"

python3 -m venv python-env
python-env/bin/pip install -r requirements.txt
python-env/bin/alembic upgrade head # Migrate our database to the latest migration

echo "Reload nginx Unit."
sudo curl -X GET --unix-socket /var/run/control.unit.sock http://localhost/control/applications/stedscare-api/restart

echo "\nDeploy script finish (deploy.sh)"