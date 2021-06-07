# Scrapy Dash Collection Helper
This is an adapter for using collections in zyte scrapy cloud. 
Its purpose is to simplify common, basic interactions with the collection.

For more advanced use cases, see the [collections API docs](https://docs.zyte.com/scrapy-cloud/collections.html) and the [pyton-scrapinghub docs](https://python-scrapinghub.readthedocs.io/en/latest/client/apidocs.html#module-scrapinghub.client.collections).

## Quickstart

Create a collection:

```python
collection = CollectionHelper(proj_id, collection_name, api_key, create=True)
```

Get a value:

```python
value = collection.get('some_key')
```

Get all items:

```python
items = collection.list_items()
```

Writing items uses the [collections batch writer](https://python-scrapinghub.readthedocs.io/en/latest/client/apidocs.html#scrapinghub.client.collections.Collection.create_writer). 
If flush is not set to true it will write batches as they fill, 
to write a partially filled batch you need to include a flush.

```python
for key, value in items_to_write:
    collection.set(key, value)
collection.flush_writer()

# write one value
# note that calling this version too often may cause timeout.
# The above method is preferred when writing multiple items
collection.set(key, value, flush=True)
```

There are various helpers to get lists of items or partial items.

```python
keys = collections.list_keys()
values = collections.list_values()
```