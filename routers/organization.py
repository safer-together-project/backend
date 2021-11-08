from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from core.database import get_db
from models.organization import Organization
from schemas.organization import OrganizationBase

router = APIRouter(
    prefix="/organization",
    responses={404: {"description": "Not found"}},
    tags=["organization"],
)

@router.get('/{access_code}', response_model=OrganizationBase, summary="Read an organization's info.")
async def read_organization(access_code: str, db: Session = Depends(get_db)):
    """
    Read an organization with all the information:

    - **name**: each organization should have a name.
    - **access_code**: should have an access code for a user to locate an organization.
    """

    organization = db.query(Organization).filter(Organization.access_code == access_code).first()
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return OrganizationBase(
                id=organization.id, 
                name=organization.name, 
                access_code=organization.access_code)