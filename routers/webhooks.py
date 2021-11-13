import os
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import Request
import subprocess

router = APIRouter(
    prefix="/webhooks",
    responses={404: {"description": "Not found"}}
)

@router.post("/", status_code=200)
async def received_payload(request: Request):
    if request.method == 'POST':
        cwd = os.getcwd()
        subprocess.Popen([f"{cwd}/bitbucket-deploy.sh"], user="deploy", shell=True)
        return 'OK'
    else:
        raise HTTPException(status_code=403, detail="You cannot access this.")

