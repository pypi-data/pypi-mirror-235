from Memora.builder.executors.find_executor import FindExecutor

class PostFindWhereAndModifier(FindExecutor):
    def __init__(self, _token: str, _collection: str, _query: str, _quantity: int, filter: dict):
        super().__init__(_token, _collection, _query, _quantity, filter)
        self.filter = filter

    def And(self, path: str, operator: any, value: any):
        self.filter['additional'].append({
            'path': path,
            'operator': operator,
            'value': value
        })
        return self