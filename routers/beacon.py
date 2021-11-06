from os import major, minor
from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.orm.session import Session

from config.database import get_db
from models.beacon import Beacon

from schemas.beacon import BeaconSchema

router = APIRouter()

@router.get('/{organization_id}', response_model=List[BeaconSchema])
async def get_beacons(organization_id: str, db: Session = Depends(get_db)):
    beacons = db.query(Beacon).filter(Beacon.organization_id == organization_id)
    return [Beacon(
                id=beacon.id, 
                organization_id=beacon.organization_id, 
                major=beacon.major,
                minor=beacon.minor,
                location=beacon.location,
                status=beacon.status) for beacon in beacons]


@router.get('/{beacon_id}', response_model=BeaconSchema)
async def get_beacon(beacon_id: str, db: Session = Depends(get_db)):
    beacon = db.query(Beacon).filter(Beacon.id == beacon_id).first()
    if beacon is None:
        raise HTTPException(status_code=404, detail="Beacon not found")

    return Beacon(
                id=beacon.id, 
                organization_id=beacon.organization_id, 
                major=beacon.major,
                minor=beacon.minor,
                location=beacon.location,
                status=beacon.status)
