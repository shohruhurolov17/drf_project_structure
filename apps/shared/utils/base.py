import uuid, base64


def generate_base64() -> None:

    uuid_bytes = uuid.uuid4().bytes

    return base64.urlsafe_b64encode(uuid_bytes).decode('utf-8').rstrip('=')
