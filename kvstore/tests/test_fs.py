import unittest
import os
import shutil
from kvstore import create
from kvstore.tests.test_base import TestBase

class TestFS(TestBase):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_files'))

    def setUp(self):
        shutil.rmtree(self.path, ignore_errors=True)

    def tearDown(self):
        pass
        #shutil.rmtree(self.path, ignore_errors=True)

    def test_all(self):
        adapter = create('file://'+self.path)
        self.run_adapter_test(adapter)


if __name__ == '__main__':
    unittest.main()
