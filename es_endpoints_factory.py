from threading import Lock
from typing import Dict, TypeVar
from config import Config
from es_endpoint import ESEndpoint

T_ESEndpoint = TypeVar("T_ESEndpoint", bound=ESEndpoint)


class ESEndpointsFactory:
    _endpoints: Dict[str, T_ESEndpoint]
    _endpoints_lock: Lock = Lock()

    @staticmethod
    def get_endpoint(config: Config):
        endpoint_id = f'{config}'
