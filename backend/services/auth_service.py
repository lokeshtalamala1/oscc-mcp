import os

def validate_user(token: str):
    #TODO: Connect to Descope SDK or validate JWT
    if token == os.getenv("DESCOPE_CLIENT_SECRET"):
        return True
    return False
