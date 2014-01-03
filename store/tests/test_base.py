import unittest

class TestBase(unittest.TestCase):
    def run_adapter_test(self, adapter):
        self.assertIsNotNone(adapter)

        file1 = '/dir1/dir2/file'
        file2 = '/dir1/dir3/file'
        data1 = u'some test data'
        data2 = u'more data'

        # file doesn't exist
        self.assertFalse(adapter.exists(file1))

        # create file
        adapter.put(file1, data1)
        # put it twice
        adapter.put(file1, data1)

        # file now exists
        self.assertTrue(adapter.exists(file1))

        # file has contents
        self.assertEqual(adapter.get(file1), data1)

        #print list(adapter.list())
        #print list(adapter.list('/'))
        #print list(adapter.list('/dir1'))
        #print list(adapter.list('/dir1/'))
        #print list(adapter.list('dir1'))
        #print list(adapter.list('/dir1/dir2'))
        #print list(adapter.list('/dir1/dir2/'))

        self.assertTrue(file1 in adapter.list())
        self.assertTrue(file1 in adapter.list('/'))
        self.assertTrue(file1 in adapter.list('/dir1'))
        self.assertTrue(file1 in adapter.list('/dir1/'))
        self.assertTrue(file1 in adapter.list('dir1'))
        self.assertTrue(file1 in adapter.list('/dir1/dir2'))
        self.assertTrue(file1 in adapter.list('/dir1/dir2/'))

        self.assertFalse(adapter.exists(file2))
        self.assertFalse(file2 in adapter.list('/dir1'))

        # create second file
        adapter.put(file2, data2)

        self.assertTrue(file2 in adapter.list('/dir1'))
        self.assertFalse(file2 in adapter.list('/dir1/dir2'))
        self.assertFalse(file1 in adapter.list('/dir1/dir3'))

        # delete
        adapter.delete(file1)
        # double delete should work
        adapter.delete(file1)

        # file doesn't exist
        self.assertFalse(adapter.exists(file1))
        self.assertRaises(KeyError, adapter.get, file1)


        self.assertTrue(file2 in adapter.list('/dir1'))
        self.assertFalse(file1 in adapter.list('/dir1'))

        adapter.delete(file2)

        self.assertFalse(file2 in adapter.list('/dir1'))
        self.assertRaises(KeyError, adapter.get, file2)
