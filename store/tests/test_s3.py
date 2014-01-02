import unittest
import os
from store import create
from boto.s3.connection import S3Connection

class TestFS(unittest.TestCase):
    path = 'pystore-test'

    def setUp(self):
        # clear the bucket
        connection = S3Connection()
        try:
            bucket = connection.get_bucket(self.path)
            for key in bucket.list():
                key.delete()
        except:
            pass

    def tearDown(self):
        # clear the bucket
        connection = S3Connection()
        try:
            bucket = connection.get_bucket(self.path)
            for key in bucket.list():
                key.delete()
        except:
            pass

    def test_all(self):
        adapter = create('s3://'+self.path)
        self.assertIsNotNone(adapter)

        filename = 'test'

        # file doesn't exist
        self.assertFalse(adapter.exists(filename))

        # create file
        data = u'some test data'
        adapter.put(filename, data)

        # file now exists
        self.assertTrue(adapter.exists(filename))

        # file has contents
        self.assertEqual(adapter.get(filename), data)

        self.assertTrue(filename in adapter.list('/'))

        # delete
        adapter.delete(filename)

        # file doesn't exist
        self.assertFalse(adapter.exists(filename))

if __name__ == '__main__':
    unittest.main()
