#!/bin/bash

echo "Deploy script start (deploy.sh)"

echo "\n\nUpdate Python Dependencies"
cd /home/deploy/steds-care-backend/
python3 -m venv python-env
source python-env/bin/activate
pip install -r requirements.txt
deactivate

echo "\nDeploy script finish (deploy.sh)"