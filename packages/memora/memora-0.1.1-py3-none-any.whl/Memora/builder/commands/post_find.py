from Memora.builder.executors.find_executor import FindExecutor
from .post_find_where import PostFindWhereModifier

class PostFindCommand(FindExecutor):
    def __init__(self, _token: str, collection: str, query: str, quantity: int):
        super().__init__(_token, collection, query, quantity)

    def where(self, path: str, operator: str, value: any):
        where_filter = {
            'path': path,
            'operator': operator,
            'value': value
        }
        
        return PostFindWhereModifier(self._token, self._collection, self._query, self._quantity, where_filter)

# We don't have an exact equivalent of JavaScript's `export` in Python,
# but we can specify in the __all__ variable what we want to be accessible
# from outside when this module is imported.

__all__ = ['PostFindCommand']
