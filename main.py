from fastapi import FastAPI

from routers.beacon import router as BeaconRouter

description = """
Steds Care App Api for our research project
"""

tags_metadata = [
    {
        "name": "beacons",
        "description": "Manages beacons from a given organization."
    }
]

api = FastAPI(
    title="StedsCareApi",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)

# Add routers here
api.include_router(BeaconRouter)

@api.on_event("startup")
async def on_startup():
    pass


@api.get("/")
async def root():
    return {"message": "Welcome to Steds Care Api. This is just to test if our api works."}

