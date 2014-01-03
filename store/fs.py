import traceback
import os, errno

class FileSystemAdapter(object):

    def __init__(self, path, **kwargs):
        self.directory = unicode(os.path.abspath(path))
        self.make_sure_path_exists(self.directory)

    def make_sure_path_exists(self, key):
        try:
            os.makedirs(key)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def key_path(self, key):
        key = unicode(key)
        if key[0] == u'/':
            key = key[1:]
        return os.path.join(self.directory, unicode(key))

    def get(self, key):
        full_path = self.key_path(key)
        try:
            with open(full_path,'r') as f:
                return f.read()
        except IOError as e:
            if e.errno == errno.ENOENT:
                raise KeyError('{}: {}'.format(key,str(e)))

    def put(self, key, data):
        full_path = self.key_path(key)
        directory = os.path.dirname(full_path)
        self.make_sure_path_exists(directory)
        with open(full_path,'w') as f:
            f.write(data)

    def delete(self, key):
        full_path = self.key_path(key)
        try:
            os.remove(full_path)
        except OSError:
            # doesn't exist
            pass

    def exists(self, key):
        full_path = self.key_path(key)
        if os.path.isfile(full_path): 
            try:
                with open(full_path,'r') as f:
                    return True
            except IOError:
                return False
        else:
            return False

    def list(self, key='/'):
        full_path = self.key_path(key)
        for directory, subdirs, files in os.walk(full_path):
            for file in files:
                path = os.path.join(directory, file)
                # remove our directory
                path = path.split(self.directory)[1]
                yield path
