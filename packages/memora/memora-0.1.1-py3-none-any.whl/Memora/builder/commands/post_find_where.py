from Memora.builder.executors.find_executor import FindExecutor
from .post_find_where_and import PostFindWhereAndModifier
from .post_find_where_or import PostFindWhereOrModifier

class PostFindWhereModifier(FindExecutor):
    def __init__(self, _token: str, _collection: str, _query: str, _quantity: int, _where_filter: dict):
        super().__init__(_token, _collection, _query, _quantity, {
            'where': _where_filter
        })
        self._where_filter = _where_filter

    def And(self, path: str, operator: str, value: any):
        filter = {
            'where': self._where_filter,
            'type': 'and',
            'additional': [{
                'path': path,
                'operator': operator,
                'value': value,
            }]
        }
        
        return PostFindWhereAndModifier(self._token, self._collection, self._query, self._quantity, filter)

    def Or(self, path: str, operator: str, value: any):
        filter = {
            'where': self._where_filter,
            'type': 'or',
            'additional': [{
                'path': path,
                'operator': operator,
                'value': value,
            }]
        }

        return PostFindWhereOrModifier(self._token, self._collection, self._query, self._quantity, filter)
