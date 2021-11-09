from fastapi.testclient import TestClient
from main import api
from core.db import override_get_db
from core.db import get_session


client = TestClient(api)

api.dependency_overrides[get_session] = override_get_db

def test_read_beacons_from_STEDS0():
    pass
