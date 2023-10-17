from Memora.builder.executors.delete_executor import DeleteExecutor

class PostDeleteCommand:
    def __init__(self, _token: str, _collection: str):
        self._token = _token
        self._collection = _collection

    def document(self, id: str):
        return DeleteExecutor(self._token, self._collection, 'document', id)

    def collection(self, name: str):
        return DeleteExecutor(self._token, self._collection, 'collection', name)
