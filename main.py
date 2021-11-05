from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/api/v1/organization/login")
async def organization_login():
    return { "hahah" : "no" }
