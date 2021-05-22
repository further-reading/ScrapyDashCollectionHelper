import scrapinghub


class Collection:
    def __init__(self, proj_id, collection_name, create=True):
        sh_client = scrapinghub.ScrapinghubClient()
        project = sh_client.get_project(proj_id)
        collections = project.collections
        self.store = collections.get_store(collection_name)
        if create:
            self.store.set({'_key': 'placeholder', 'value': 123})
            self.store.delete(['placeholder'])

    def get(self, key, default=None):
        search = self.store.list([key])
        if not search:
            return default
        return search[0]['value']


collection = Collection(394499, 'twitch')
