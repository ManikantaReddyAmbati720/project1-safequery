from src.validator import validate

def test_delete_blocked():
    valid, msg = validate("DELETE FROM users")
    assert not valid