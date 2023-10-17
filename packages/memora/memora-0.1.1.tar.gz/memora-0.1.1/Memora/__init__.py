from Memora.builder.commands.command import Command

class Memora(Command):
    def __init__(self, _token: str = '', _collection: str = 'personal'):
        super().__init__(_token, _collection)
        self._token = _token
        self._debug = False

    def __debug_on(self):
        self._debug = True

    def on(self, collection: str) -> 'Command':
        return Command(self._token, collection)

def auth(token: str):
    memora = Memora(token)
    return memora

# memora.within('codefiles').add('aoao').go()

# Into: memora.into('collection-name').add('doc1').go()
# Inside: memora.inside('collection-name').add('doc1').go()
# Within: memora.within('collection-name').add('doc1').go()
# On: memora.on('collection-name').add('doc1').go()
# At: memora.at('collection-name').add('doc1').go()
# Using: memora.using('collection-name').add('doc1').go()
# Access: memora.access('collection-name').add('doc1').go()