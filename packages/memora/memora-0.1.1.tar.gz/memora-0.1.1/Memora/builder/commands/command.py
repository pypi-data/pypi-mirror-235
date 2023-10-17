from typing import Union, List
from .post_add import PostAddCommand
from .post_add_batch import PostAddBatchCommand
from .post_delete import PostDeleteCommand
from .post_find import PostFindCommand

class Command:
    def __init__(self, __token: str, _collection: str):
        self._token = __token
        self._collection = _collection

    def delete(self):
        return PostDeleteCommand(self._token, self._collection)

    def add(self, content: Union[str, List[str]]):
        if isinstance(content, list):
            for c in content:
                if len(c) == 0:
                    raise ValueError('Document content cannot be empty and you tried passing an empty content string.')
            return PostAddBatchCommand(self._token, self._collection, content)

        if len(content) == 0:
            raise ValueError('Document content cannot be empty and you tried passing an empty content string.')

        return PostAddCommand(self._token, 'personal', content)

    def find(self, query: str, quantity: int = 3):
        return PostFindCommand(self._token, self._collection, query, quantity)

# We don't have an exact equivalent of JavaScript's `export` in Python,
# but we can specify in the __all__ variable what we want to be accessible
# from outside when this module is imported.

__all__ = ['Command']
