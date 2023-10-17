from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    client_secret: Optional[str] = None

    log_loc: Optional[str] = None
    promt: bool = True
    auth_host: str = "https://auth.dev.origen.ai"
    api_host: str = "https://proteus-test.dev.origen.ai"
    api_host_v2: Optional[str] = None
    vault_host: str = "https://vault.dev.origen.ai"
    username: str = "user-not-configured"
    password: str = "password-not-configured"
    realm: str = "origen"
    client_id: str = "proteus-front"
    refresh_gap: int = 10  # Seconds
    ignore_worker_status: bool = False
    upload_presigned: bool = True
    ssl_verify: bool = True
    default_retry_times: int = 5
    default_retry_wait: float = 0.5  # s
    default_timeout = 30  # s
    worker_uuid: Optional[str] = None
