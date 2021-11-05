#!/bin/bash

echo "Deploy script start (deploy.sh)"

echo "\n\nUpdate Python Dependencies"

cd /home/deploy/steds-care-backend/
python3 -m venv python-env
python-env/bin/pip install -r requirements.txt


echo "\nDeploy script finish (deploy.sh)"