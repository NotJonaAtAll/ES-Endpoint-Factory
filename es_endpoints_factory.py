from threading import Lock
from typing import Dict, Type, TypeVar
from config import Config
from es_endpoint import ESEndpoint

T_ESEndpoint = TypeVar("T_ESEndpoint", bound=ESEndpoint)


class ESEndpointsFactory:
    _instance: "ESEndpointsFactory" = None
    _singleton_lock: Lock = Lock()
    _is_initialized: bool = False

    _endpoints_type: Type[T_ESEndpoint]

    _endpoints: Dict[str, T_ESEndpoint]
    _endpoints_lock: Lock = Lock()

    def __init__(self, endpoints_type: Type[T_ESEndpoint] = ESEndpoint) -> None:
        if ESEndpointsFactory._is_initialized:
            return

        ESEndpointsFactory._endpoints_type = endpoints_type

        ESEndpointsFactory._is_initialized = True

    def __new__(cls: Type["ESEndpointsFactory"]):
        if cls._instance is None:
            with cls._singleton_lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def get_endpoint(config: Config):
        endpoint_id = f'{config.host}:{config.port}'

        if not ESEndpointsFactory._is_initialized:
            ESEndpointsFactory()

        if endpoint_id not in ESEndpointsFactory._endpoints.keys():
            with ESEndpointsFactory._endpoints_lock:
                if endpoint_id not in ESEndpointsFactory._endpoints.keys():
                    ESEndpointsFactory._endpoints[endpoint_id] = ESEndpointsFactory._endpoints_type(config)
