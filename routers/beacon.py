from typing import List
from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.beacon import Beacon, BeaconCreate, BeaconRead
from utils.handle_errors import handle_integrity_error


router = APIRouter(
    prefix="/beacons",
    responses={404: {"description": "Not found"}},
    tags=["beacons"],
)

@router.get('/{organization_id}', response_model=List[BeaconRead], summary="Manages beacons from a given organization.")
async def read_beacons(organization_id: str, session: AsyncSession = Depends(get_session)):
    """
    Read beacons with all the information:

    - **major**: the main identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """
    
    statement = select(Beacon).where(Beacon.organization_id == organization_id)
    results = await session.execute(statement)
    beacons = results.scalars().all()
    return beacons

@router.get('/beacon/{beacon_id}', response_model=BeaconRead, summary="A single beacon that reports status and location.")
async def read_beacon(beacon_id: str, beacon_major: int, beacon_minor: int, session: AsyncSession = Depends(get_session)):
    """
    Read a beacon with all the information:

    - **major**: the main identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """

    statement = select(Beacon).where(Beacon.id == beacon_id).where(Beacon.major == beacon_major).where(Beacon.minor == beacon_minor)
    result = await session.execute(statement)

    beacon = result.scalar_one_or_none()

    if beacon is None:
        raise HTTPException(status_code=404, detail="Beacon not found")

    return beacon

@router.post('/beacon/', response_model=BeaconRead)
async def create_beacon(beacon: BeaconCreate, session: AsyncSession = Depends(get_session)):
    """
    Create a beacon with:

    - **id**: the main identification
    - **major**: the submain identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """

    try:
        db_beacon = Beacon.from_orm(beacon)
        session.add(db_beacon)
        await session.flush()
        await session.refresh(db_beacon)
    except IntegrityError as error:
        await session.rollback()
        handle_integrity_error(error)
    else:
        await session.commit()
    
    return db_beacon
