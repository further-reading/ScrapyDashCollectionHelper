import scrapinghub


class Collection:
    def __init__(self, proj_id, collection_name, create=False):
        sh_client = scrapinghub.ScrapinghubClient()
        project = sh_client.get_project(proj_id)
        collections = project.collections
        self.store = collections.get_store(collection_name)
        self.writer = self.store.create_writer()
        if create:
            self.store.set({'_key': 'placeholder', 'value': 123})
            self.store.delete(['placeholder'])

    def get(self, key, default=None):
        search = self.store.list([key])
        if not search:
            return default
        return search[0]['value']

    def set(self, key, value, flush=False):
        self.writer.write({'_key': key, 'value': value})
        if flush:
            self.writer.flush()
