from typing import Any, NoReturn, Union
from typing_extensions import TypedDict
from os import getenv


class _Config(TypedDict):
    user: str
    password: str
    host: str
    port: int
    timeout: int
    es_cert_path: str


class Config(dict):
    def __init__(self, config: _Config = None, json_path: str = None):
        super().__init__()

        if config is not None:
            self.__populate(config)
        elif json_path is not None:
            self.__populate(Config.__from_json(json_path))
        else:
            self.__populate(Config.__from_env())

    def __populate(self, config: _Config):
        for k, v in config.item():
            self[k] = v

    @staticmethod
    def __from_json(json_path: str) -> _Config:
        pass

    @staticmethod
    def __from_env() -> _Config:
        try:
            return {
                "user": Config.__get_env_var("ES_USER"),
                "password": Config.__get_env_var("ES_PASSWORD"),
                "host": Config.__get_env_var("ES_HOST"),
                "port": int(Config.__get_env_var("ES_PORT")),
                "timeout": int(Config.__get_env_var("ES_TIMEOUT")),
                "es_cert_path": Config.__get_env_var("ES_CERT_PATH"),
            }
        except KeyError as e:
            print(f"No such environment variable {e.args[1]}")
            return None

    @staticmethod
    def __get_env_var(key: str) -> Union[str, NoReturn]:
        value = getenv(key, None)

        if value is None:
            raise KeyError("No such environment variable", key)

        return value

    @property
    def user(self) -> str:
        return self["user"]

    @property
    def password(self) -> str:
        return self["password"]

    @property
    def host(self) -> str:
        return self["host"]

    @property
    def port(self) -> int:
        return self["port"]

    @property
    def timeout(self) -> int:
        return self["timeout"]

    @property
    def es_cert_path(self) -> str:
        return self["es_cert_path"]
