from fastapi import FastAPI

from routers.organization import router as OrganizationRouter
from routers.beacon import router as BeaconRouter
from routers.report import router as ReportRouter
from routers.path import router as PathRouter
from routers.point import router as PointRouter
from routers.webhooks import router as WebhooksRouter

description = """
Steds Care App Api for our research project
"""

api = FastAPI(
    title="StedsCareApi",
    description=description,
    version="0.0.1"
)

# Add routers here
api.include_router(OrganizationRouter)
api.include_router(BeaconRouter)
api.include_router(ReportRouter)
api.include_router(PathRouter)
api.include_router(PointRouter)

# Webhook router
api.include_router(WebhooksRouter)

@api.get("/")
async def root():
    return {"message": "Welcome to Steds Care Api. This is just to test if our api works."}

