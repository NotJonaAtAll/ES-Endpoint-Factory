from elasticsearch import Elasticsearch

from es_endpoints_factory.config import Config


class ESEndpoint(Elasticsearch):
    def __init__(self, config: Config):
        super().__init__(
            hosts=[f"{config.host}:{config.port}"],
            # http_auth=("user", "pass"),
            # use_ssl=True,
            # verify_certs=True,
            # ca_certs=""
        )
        self.config = config
