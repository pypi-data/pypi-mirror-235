from typing import Any, Dict, List, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
from .add_executor import AddExecutor
from Memora.app_error import AppError

class AddBatchExecutor:
    def __init__(self, _token: str, _collection: str, _content: List[str], _metadata: List[Dict[str, Any]] = None):
        self._token = _token
        self._collection = _collection
        self._content = _content
        self._metadata = _metadata

    def go(self):
        promises = []
        for i in range(len(self._content)):
            executor = AddExecutor(self._token, self._collection, self._content[i], self._metadata[i] if self._metadata else None)
            promises.append(executor.go())

        # Concurrent execution of promises
        ids = []
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(promise) for promise in promises}
            for future in as_completed(futures):
                try:
                    result = future.result()
                    ids.append({'id': result, 'success': True})
                except AppError as e:
                    print(e)
                    ids.append({'error': str(e), 'success': False})
                except Exception as e:
                    ids.append({'error': str(e), 'success': False})
        return ids
