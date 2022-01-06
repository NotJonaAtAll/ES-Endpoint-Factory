from elasticsearch import Elasticsearch


class _ESEndpoint(Elasticsearch):
    def __init__(self):
        super().__init__()
