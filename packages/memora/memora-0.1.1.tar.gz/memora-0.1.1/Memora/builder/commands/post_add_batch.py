from typing import Any, Dict, List
from Memora.builder.executors.add_batch_executor import AddBatchExecutor

class PostAddBatchCommand(AddBatchExecutor):
    def __init__(self, _token: str, _collection: str, _content: List[str]):
        super().__init__(_token, _collection, _content)

    def metadata(self, metadata: List[Dict[str, Any]]):
        if len(metadata) != len(self._content):
            raise ValueError('The length of metadata must be equal to the length of content')
        return AddBatchExecutor(self._token, self._collection, self._content, metadata)
