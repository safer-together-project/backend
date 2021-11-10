from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.organization import Organization

router = APIRouter(
    prefix="/organization",
    responses={404: {"description": "Not found"}},
    tags=["organization"],
)

@router.get('/{access_code}', response_model=Organization, summary="Read an organization's info.")
async def read_organization(access_code: str, session: AsyncSession = Depends(get_session)):
    """
    Read an organization with all the information:

    - **name**: each organization should have a name.
    - **access_code**: should have an access code for a user to locate an organization.
    """
    statement = select(Organization).where(Organization.access_code == access_code)
    result = await session.execute(statement)

    organization = result.first()
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return organization