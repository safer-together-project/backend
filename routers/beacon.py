from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from core.db import get_session
from models.beacon import Beacon


router = APIRouter(
    prefix="/beacons",
    responses={404: {"description": "Not found"}},
    tags=["beacons"],
)

@router.get('/{organization_id}', response_model=List[Beacon], summary="Manages beacons from a given organization.")
async def read_beacons(organization_id: str, session: Session = Depends(get_session)):
    """
    Read beacons with all the information:

    - **major**: the main identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """
    with session:
        statement = select(Beacon).where(Beacon.organization_id == organization_id)
        result = session.exec(statement)
        return result.all()

@router.get('/beacon/{beacon_id}', response_model=Beacon, summary="A single beacon that reports status and location.")
async def read_beacon(beacon_id: str, session: Session = Depends(get_session)):
    """
    Read a beacon with all the information:

    - **major**: the main identification.
    - **minor**: the unique identification.
    - **status**: the status of the beacon
    """

    with session:
        statement = select(Beacon).where(Beacon.id == beacon_id)
        result = session.exec(statement)

        beacon = result.first()
        if beacon is None:
            raise HTTPException(status_code=404, detail="Organization not found")

        return beacon
