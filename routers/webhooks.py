from fastapi import APIRouter, HTTPException, Request
import httpx
import asyncio

router = APIRouter(
    prefix="/webhooks",
    responses={404: {"description": "Not found"}}
)

async def request(client):
    response = await client.post("http://0.0.0.0:9000/hooks/redeploy-webhook")
    return "ok"


@router.post("/", status_code=200)
async def received_payload(requests: Request):
    if requests.method == 'POST':
        async with httpx.AsyncClient() as client:
            tasks = [request(client)]
            result = await asyncio.gather(*tasks)
            return result
    else:
        raise HTTPException(status_code=403, detail="You cannot access this.")

