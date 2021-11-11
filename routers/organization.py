from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.db import get_session
from models.organization import Organization, OrganizationCreate, OrganizationRead

router = APIRouter(
    prefix="/organization",
    responses={404: {"description": "Not found"}},
    tags=["organization"],
)

@router.get('/{access_code}', response_model=OrganizationRead, summary="Read an organization's info.")
async def read_organization(access_code: str, session: AsyncSession = Depends(get_session)):
    """
    Read an organization with all the information:

    - **name**: each organization should have a name.
    - **access_code**: should have an access code for a user to locate an organization.
    """
    statement = select(Organization).where(Organization.access_code == access_code)
    result = await session.execute(statement)

    organization = result.scalar_one_or_none()
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")

    return organization

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OrganizationRead)
async def create_organizaton(organization: OrganizationCreate, session: AsyncSession = Depends(get_session)):
    try:
        session.add(organization)
        await session.flush()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Organization already created with the same access code.")
    else:
        await session.commit()
    return organization