from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from config.database import get_db
from models.organization import Organization
from schemas.organization import OrganizationBase

router = APIRouter(
    prefix="/organizations",
    responses={404: {"description": "Not found"}},
)

@router.get('/{access_code}', response_model=OrganizationBase, tags=["organization"])
async def read_organization(access_code: str, db: Session = Depends(get_db)):
    organization = db.query(Organization).filter(Organization.access_code == access_code).first()
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return OrganizationBase(
                id=organization.id, 
                name=organization.name, 
                access_code=organization.access_code)