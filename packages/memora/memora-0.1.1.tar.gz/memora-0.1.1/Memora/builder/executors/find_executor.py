from Memora.app_error import AppError
from Memora.services.memoraFetch import memoraFetch

class FindExecutor:
    def __init__(self, token, collection, query, quantity, filters=None):
        self._token = token
        self._collection = collection
        self._query = query
        self._quantity = quantity
        self._filters = filters

    def go(self):
        body = {
            'query': self._query,
        }

        if self._filters:
            filter = {}
            if 'type' in self._filters:
                filters = []
                filter[self._filters['type']] = filters

                filters.append({
                    'key': self._filters['where']['path'],
                    'op': self._filters['where']['operator'],
                    'value': self._filters['where']['value'],
                })

                for f in self._filters['additional']:
                    filters.append({
                        'key': f['path'],
                        'op': f['operator'],
                        'value': f['value'],
                    })
            else:
                filter['and'] = [{
                    'key': self._filters['where']['path'],
                    'op': self._filters['where']['operator'],
                    'value': self._filters['where']['value'],
                }]

            body['filters'] = filter

        res = memoraFetch(
            self._token,
            f'collections/{self._collection}/search?limit={self._quantity}',
            'POST',
            body
        )

        if res.status_code != 200:
            if res.status_code == 400:
                json = res.json()
                if 'message' in json:
                    raise AppError(json)
            json = res.json()
            print(json)
            print(self._token)
            print(res)
            raise Exception('Error while searching')

        json = res.json()
        return json['documents']