import mimetypes

class S3Adapter(object):
    def __init__(self, path, **kwargs):
        from boto.s3.connection import S3Connection
        self.connection = S3Connection(**kwargs)

        self.path = unicode(path)
        if not self.connection.lookup(self.path):
            self.connection.create_bucket(self.path)
        self.bucket = self.connection.get_bucket(self.path, validate=False)

    def key_path(self, key):
        if key[0] != u'/':
            key = u'/'+key
        return key

    def get(self, key):
        full_path = self.key_path(key)
        k = self.bucket.get_key(full_path)
        if not k:
            raise KeyError('Key not found: {}'.format(key))
        return k.get_contents_as_string()

    def put(self, key, data, mime=None, **kwargs):
        from boto.s3.key import Key
        full_path = self.key_path(key)
        k = Key(self.bucket)
        k.key = full_path
        if isinstance(mime, basestring):
            k.set_metadata("Content-Type", mime)
        elif mime == True:
            # guess mime type
            mime = mimetypes.guess_type(key)[0]
            if mime:
                k.set_metadata("Content-Type", mime)
        k.set_contents_from_string(data)

    def delete(self, key):
        from boto.s3.key import Key
        full_path = self.key_path(key)
        k = Key(self.bucket)
        k.name = full_path
        k.delete()

    def exists(self, key):
        full_path = self.key_path(key)
        return self.bucket.get_key(full_path) is not None

    def list(self, key=u'/'):
        # we need slightly different paths for listing
        # ensure we end in a /
        if key[-1] != u'/':
            key = key+u'/'
        # ensure we don't start in a /
        if key[0] == u'/':
            key = key[1:]
        for k in self.bucket.list(prefix=key):
            name = k.name
            # ensure we start with a /
            if name[0] != u'/':
                name = u'/'+name
            yield name

    def drop_all(self):
        self.bucket.delete_keys([key.name for key in self.bucket])
