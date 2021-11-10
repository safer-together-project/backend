from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from models.beacon import Beacon


router = APIRouter(
    prefix="/beacons",
    responses={404: {"description": "Not found"}},
    tags=["beacons"],
)

@router.get('/{organization_id}', response_model=List[Beacon], summary="Manages beacons from a given organization.")
async def read_beacons(organization_id: str, session: AsyncSession = Depends(get_session)):
    """
    Read beacons with all the information:

    - **major**: the main identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """
    
    statement = select(Beacon).where(Beacon.organization_id == organization_id)
    results = await session.execute(statement)
    beacons = results.all()
    return beacons

@router.get('/beacon/{beacon_id}', response_model=Beacon, summary="A single beacon that reports status and location.")
async def read_beacon(beacon_id: str, session: AsyncSession = Depends(get_session)):
    """
    Read a beacon with all the information:

    - **major**: the main identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """

    statement = select(Beacon).where(Beacon.id == beacon_id)
    result = await session.execute(statement)

    beacon = result.first()

    if beacon is None:
        raise HTTPException(status_code=404, detail="Beacon not found")

    return beacon
