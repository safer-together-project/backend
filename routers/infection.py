from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.db import get_session
from models.infection import Infection, InfectionCreate, InfectionRead, InfectionUpdate
from utils.handle_errors import handle_integrity_error

router = APIRouter(
    prefix="/infections",
    responses={404: {"description": "Not found"}},
    tags=["infection"],
)

@router.get('', response_model=List[InfectionRead], summary="Read all infections in the db.")
async def read_infections(session: AsyncSession = Depends(get_session)):
    """
    Read all infections with all the information:

    - **name**: each infection should have a name.
    - **type**: type of infection.
    """
    statement = select(Infection)
    result = await session.execute(statement)

    points = result.scalars().all()
    return points

@router.get('/infection/{infection_id}', response_model=InfectionRead, summary="Read an infection's info.")
async def read_infection(infection_id: str, session: AsyncSession = Depends(get_session)):
    """
    Read an infection with all the information:

    - **name**: each infection should have a name.
    - **type**: type of infection.
    """
    statement = select(Infection).where(Infection.id == infection_id)
    result = await session.execute(statement)

    infection = result.scalar_one_or_none()
    if infection is None:
        raise HTTPException(status_code=404, detail="Infection not found")

    return infection

@router.post('/infection', status_code=status.HTTP_201_CREATED, response_model=InfectionRead)
async def create_infection(infection: InfectionCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_infection = infection.from_orm(infection)
        session.add(db_infection)
        await session.flush()
        await session.refresh(db_infection)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_infection

@router.patch('/infection/{infection_id}', status_code=status.HTTP_200_OK, response_model=InfectionUpdate)
async def update_infection(infection_id: int, infection: InfectionUpdate, session: AsyncSession = Depends(get_session)):
    try:
        db_infection = session.get(infection_id)
        if not db_infection:
            raise HTTPException(status_code=404, detail="infection not found")

        infection_data = infection.dict(exclude_unset=True)
        for key, value in infection_data.items():
            setattr(db_infection, key, value)
        session.add(db_infection)
        await session.flush()
        await session.refresh(db_infection)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_infection
