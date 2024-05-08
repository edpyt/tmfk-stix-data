import uuid
import hashlib


def create_uuid_from_string(val: str) -> uuid.UUID:
    hex_string = hashlib.md5(val.encode("UTF-8")).hexdigest()
    return uuid.UUID(hex=hex_string, version=4)
