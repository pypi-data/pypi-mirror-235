from Memora.services.memoraFetch import memoraFetch

class DeleteExecutor:
    def __init__(self, _token: str, _collection: str, _type: str, _id: str):
        self._token = _token
        self._collection = _collection
        self._type = _type
        self._id = _id

    def go(self):
        obj = {
            'operation': 'delete',
            'type': self._type,
            'id': self._id
        }

        if self._type == 'collection':
            res = memoraFetch(
                self._token,
                f'collections/{self._id}',
                'DELETE'
            )

            if res.status_code >= 300:
                raise ValueError(f'Was not able to delete your document (status {res.status_code})')

            return True

        elif self._type == 'document':
            res = memora_fetch(
                self._token,
                f'collections/{self._collection}/documents/{self._id}',
                'DELETE'
            )

            if res.status_code >= 300:
                raise ValueError(f'Was not able to delete your document (status {res.status_code})')

            return True
