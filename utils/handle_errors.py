from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status

def handle_integrity_error(error: IntegrityError):
    db_status_code = error.orig.args[0]
    db_message = error.orig.args[1]
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"Error Code": db_status_code, "Message": db_message})
