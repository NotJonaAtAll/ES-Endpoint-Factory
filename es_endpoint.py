from elasticsearch import Elasticsearch

from config import Config


class ESEndpoint(Elasticsearch):
    def __init__(self, config: Config):
        super().__init__()
