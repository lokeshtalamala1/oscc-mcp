from backend.services.auth_service import validate_user

def test_validate_user():
    assert validate_user("wrong") is False
