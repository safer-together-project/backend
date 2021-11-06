zfrom fastapi import FastAPI

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

@api.get("/")
async def root():
    return {"message": "Welcome to Steds Care Api. This is just to test if our api works."}


# Beacons

@api.get("/api/v1/beacons/", tags=["beacons"])
async def get_beacons():
    return { "hahah" : "no" }


@api.get("/api/v1/organization/login")
async def organization_login():
    return { "hahah" : "no" }
