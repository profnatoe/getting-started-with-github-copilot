import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture()
def client():
    """Provide a TestClient with isolated in-memory activity data per test."""
    original_activities = copy.deepcopy(activities)
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        activities.clear()
        activities.update(copy.deepcopy(original_activities))
