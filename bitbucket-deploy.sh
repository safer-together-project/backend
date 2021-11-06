#!/bin/bash

echo "Deploy script start (deploy.sh)"

echo "\n\nUpdate Python Dependencies"

cd /home/deploy/steds-care-backend/
python3 -m venv python-env
python-env/bin/pip install -r requirements.txt


echo "Reload nginx Unit."
sudo curl -X GET --unix-socket /var/run/control.unit.sock http://localhost/control/applications/stedscare-api/restart

echo "\nDeploy script finish (deploy.sh)"