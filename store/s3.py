
class S3Adapter(object):
    def __init__(self, path, aws_access_key=None, aws_secret_key=None, **kwargs):
        from boto.s3.connection import S3Connection
        self.connection = S3Connection(aws_access_key, aws_secret_key)

        if not self.connection.lookup(path):
            self.connection.create_bucket(path)
        self.bucket = self.connection.get_bucket(path, validate=False)

    def get(self, path):
        key = self.bucket.get_key(path)
        if not key:
            raise KeyError('Key not found: {}'.format(path))
        key.open('r')
        return key.read()

    def put(self, path, data):
        from boto.s3.key import Key
        key = Key(self.bucket)
        key.key = path
        key.set_contents_from_string(data)

    def delete(self, path):
        from boto.s3.key import Key
        key = Key(self.bucket)
        key.name = path
        key.delete()

    def exists(self, path):
        return self.bucket.get_key(path) is not None

    def list(self, path):
        if path == '/':
            path = None
        for key in self.bucket.list(prefix=path, delimiter='/'):
            if key.name == path:
                continue
            yield key.name
