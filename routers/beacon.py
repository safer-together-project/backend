from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from config.database import get_db
from models.beacon import Beacon

from schemas.beacon import BeaconBase

router = APIRouter(
    prefix="/beacons",
    responses={404: {"description": "Not found"}},
)

@router.get('/{organization_id}', response_model=List[BeaconBase], tags=["beacons"])
async def read_beacons(organization_id: str, db: Session = Depends(get_db)):
    beacons = db.query(Beacon).filter(Beacon.organization_id == organization_id)
    return [BeaconBase(
                id=beacon.id, 
                organization_id=beacon.organization_id,
                major=beacon.major,
                minor=beacon.minor,
                status=beacon.status) for beacon in beacons]

@router.get('/beacon/{beacon_id}', response_model=BeaconBase, tags=["beacon"])
async def read_beacon(beacon_id: str, db: Session = Depends(get_db)):
    beacon = db.query(Beacon).filter(Beacon.id == beacon_id).first()
    if beacon is None:
        raise HTTPException(status_code=404, detail="Beacon not found")

    return BeaconBase(
                id=beacon.id, 
                organization_id=beacon.organization_id, 
                major=beacon.major,
                minor=beacon.minor,
                status=beacon.status)