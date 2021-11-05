from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/api/v1/organization/login")
async def organization_login():
    return { "hahah" : "no" }



# # NGINX Unit Application
# async def application(scope, receive, send):

#     await send({
#         'type': 'http.response.start',
#         'status': 200
#     })

#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, ASGI\n'
#     })
