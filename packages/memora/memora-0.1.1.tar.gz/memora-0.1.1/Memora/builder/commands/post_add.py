from typing import Any, Dict
from Memora.builder.executors.add_executor import AddExecutor

class PostAddCommand(AddExecutor):
    def __init__(self, _token: str, _collection: str, _content: str):
        super().__init__(_token, _collection, _content)

    def metadata(self, metadata: Dict[str, Any]):
        return AddExecutor(self._token, self._collection, self._content, metadata)
