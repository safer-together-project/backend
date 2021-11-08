from fastapi.testclient import TestClient
from ..main import api
from ..core.database import override_get_db
from ..core.database import get_db


client = TestClient(api)

api.dependency_overrides[get_db] = override_get_db

def test_read_beacons_from_STEDS0():
    pass
