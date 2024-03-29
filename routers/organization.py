from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.db import get_session
from models.organization import Organization, OrganizationCreate, OrganizationRead, OrganizationUpdate
from utils.handle_errors import handle_integrity_error

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

@router.post('', status_code=status.HTTP_201_CREATED, response_model=OrganizationRead)
async def create_organizaton(organization: OrganizationCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_organizaton = Organization.from_orm(organization)
        session.add(db_organizaton)
        await session.flush()
        await session.refresh(db_organizaton)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_organizaton

@router.patch('/{organization_id}', status_code=status.HTTP_200_OK, response_model=OrganizationUpdate)
async def update_organization(organization_id: int, organization: OrganizationUpdate, session: AsyncSession = Depends(get_session)):
    try:
        db_organizaton = session.get(organization_id)
        if not db_organizaton:
            raise HTTPException(status_code=404, detail="Organization not found")

        organization_data = organization.dict(exclude_unset=True)
        for key, value in organization_data.items():
            setattr(db_organizaton, key, value)
        session.add(db_organizaton)
        await session.flush()
        await session.refresh(db_organizaton)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_organizaton
