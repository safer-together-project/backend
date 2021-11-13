from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from starlette.requests import Request


router = APIRouter(
    prefix="/webhooks",
    responses={404: {"description": "Not found"}}
)

@router.post("/", status_code=200)
async def received_payload(
    request: Request,
):

   if request.method == 'POST':
      data = await request.json()
      commit_author = data['actor']['username']
      commit_hash = data['push']['changes'][0]['new']['target']['hash'][:7]
      commit_url = data['push']['changes'][0]['new']['target']['links']['html']['href']
      print('Webhook received! %s committed %s' % (commit_author, commit_hash))
      return 'OK'
   else:
      raise HTTPException(status_code=403, detail="You cannot access this.")

