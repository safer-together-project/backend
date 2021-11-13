from fastapi import APIRouter
from starlette.requests import Request


router = APIRouter(
    prefix="/webhooks",
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def received_payload(
    request: Request,
):
    payload = await request.json()

    default_branch = payload["repository"]
    if default_branch != None:
        # script_name = DEPLOY_SCRIPTS[app_name]
        # # background_tasks.add_task(deploy_application, script_name)
        return {"message": "Deployment started"}

    else:
        return {"message": "Unable to process action"}

