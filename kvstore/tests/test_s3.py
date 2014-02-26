import unittest
import os
from kvstore import create
from boto.s3.connection import S3Connection
from kvstore.tests.test_base import TestBase

class TestS3(TestBase):
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
        self.run_adapter_test(adapter)

if __name__ == '__main__':
    unittest.main()
