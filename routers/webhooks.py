from fastapi import APIRouter
from starlette.requests import Request


router = APIRouter(
    prefix="/webhooks",
    responses={404: {"description": "Not found"}}
)

@router.post("/", status_code=200)
async def received_payload(
    request: Request,
):
    return "Hi" 

