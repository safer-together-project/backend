from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from core.db import get_session
from models.infection_condition import InfectionCondition, InfectionConditionCreate, InfectionConditionRead, InfectionConditionReadWithInfection, InfectionConditionUpdate
from utils.handle_errors import handle_integrity_error

router = APIRouter(
    prefix="/infection_conditions",
    responses={404: {"description": "Not found"}},
    tags=["infection_conditions"],
)

@router.get('/{organization_id}', response_model=List[InfectionConditionReadWithInfection], summary="Read all infections conditions in the db.")
async def read_infection_conditions(organization_id: int, session: AsyncSession = Depends(get_session)):
    """
    Read all infection conditions with all the information:
    """
    statement = select(InfectionCondition).where(InfectionCondition.organization_id == organization_id).options(selectinload(InfectionCondition.infection))
    result = await session.execute(statement)

    points = result.scalars().all()
    return points

@router.get('/condition/{infection_condition_id}', response_model=InfectionConditionReadWithInfection, summary="Read an infection condition's info.")
async def read_infection_condition(infection_condition_id: str, session: AsyncSession = Depends(get_session)):
    """
    Read an infection condition with all the information:
    """
    statement = select(InfectionCondition).where(InfectionCondition.id == infection_condition_id)
    result = await session.execute(statement)

    infection_condition = result.scalar_one_or_none()
    if infection_condition is None:
        raise HTTPException(status_code=404, detail="Infection Condition not found")

    return infection_condition

@router.post('/condition', status_code=status.HTTP_201_CREATED, response_model=InfectionConditionRead)
async def create_infection_condition(infection: InfectionConditionCreate, session: AsyncSession = Depends(get_session)):
    try:
        db_infection_condition = InfectionCondition.from_orm(infection)
        session.add(db_infection_condition)
        await session.flush()
        await session.refresh(db_infection_condition)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_infection_condition

@router.patch('/condition/{infection_condition_id}', status_code=status.HTTP_200_OK, response_model=InfectionConditionUpdate)
async def update_infection_condition(infection_condition_id: int, infection: InfectionConditionUpdate, session: AsyncSession = Depends(get_session)):
    try:
        db_infection_condition = session.get(infection_condition_id)
        if not db_infection_condition:
            raise HTTPException(status_code=404, detail="infection not found")

        infection_data = infection.dict(exclude_unset=True)
        for key, value in infection_data.items():
            setattr(db_infection_condition, key, value)
        session.add(db_infection_condition)
        await session.flush()
        await session.refresh(db_infection_condition)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    return db_infection_condition
