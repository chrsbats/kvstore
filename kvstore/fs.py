from __future__ import absolute_import
import traceback
import os, errno
import shutil
from .signal import interrupt_protect

class FileSystemAdapter(object):

    def __init__(self, path, **kwargs):
        # expand ~ or we'll end up creating a /~ directory
        # abspath doesn't do this for us
        self.path = os.path.abspath(os.path.expanduser(path))
        self.make_sure_path_exists(self.path)

    def make_sure_path_exists(self, key):
        try:
            os.makedirs(key)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def key_path(self, key):
        key = key
        if key[0] == '/':
            key = key[1:]
        return os.path.join(self.path, key)

    def get(self, key):
        full_path = self.key_path(key)
        try:
            with open(full_path,'r') as f:
                return f.read()
        except IOError as e:
            if e.errno == errno.ENOENT:
                raise KeyError('{}: {}'.format(key,str(e)))
            raise

    @interrupt_protect
    def put(self, key, data, **kwargs):
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
                if file[0] == '.':
                    continue
                path = os.path.join(directory, file)
                # remove our directory
                path = path.split(self.path)[1]
                yield path

    def drop_all(self):
        # delete the directory and then recreate it
        shutil.rmtree(self.path, ignore_errors=True)
        self.make_sure_path_exists(self.path)
