from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_hash(password: str):
    return pwd_context.hash(password)

def verify_hash(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)
