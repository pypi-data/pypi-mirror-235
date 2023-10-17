from Memora.services.memoraFetch import memoraFetch
from Memora.app_error import AppError

class AddExecutor:
    def __init__(self, _token, _collection, _content, _metadata=None):
        self._token = _token
        self._collection = _collection
        self._content = _content
        self._metadata = _metadata

    def go(self):
        body = {
            'content': self._content,
        }

        if self._metadata:
            body['metadata'] = self._metadata
        else:
            body['metadata'] = {}

        res = memoraFetch(
            self._token,
            f'collections/{self._collection}/documents',
            'POST',
            body
        )

        if res.status_code >= 300:
            if res.status_code == 400:
                json_data = res.json()
                if 'message' in json_data:
                    raise AppError(json_data)
            raise Exception('Error adding document')

        json_data = res.json()
        id_ = json_data['id']
        return id_
