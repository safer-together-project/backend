from fastapi import FastAPI
from core.config import Config

from routers.beacon import router as BeaconRouter
from routers.organization import router as OrganizationRouter
from routers.report import router as ReportRouter
from routers.path import router as PathRouter
from routers.point import router as PointRouter

description = """
Steds Care App Api for our research project
"""

tags_metadata = [
    {
        "name": "beacons",
        "description": "Manages beacons from a given organization."
    },
    {
        "name": "beacon",
        "description": "A single beacon that reports status and location."
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
api.include_router(OrganizationRouter)
api.include_router(ReportRouter)
api.include_router(PathRouter)
api.include_router(PointRouter)

@api.get("/")
async def root():
    return {"message": "Welcome to Steds Care Api. This is just to test if our api works."}

