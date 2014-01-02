import unittest
import os
import shutil
from store import create

class TestFS(unittest.TestCase):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_files'))

    def setUp(self):
        shutil.rmtree(self.path, ignore_errors=True)

    def tearDown(self):
        shutil.rmtree(self.path, ignore_errors=True)

    def test_all(self):
        adapter = create('file://'+self.path)
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
