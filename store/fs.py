import traceback
import os, errno

class FileSystemAdapter(object):

    def __init__(self, path, **kwargs):
        if path[-1] != '/':
            path = path + '/'
        self.directory = path
        self.make_sure_path_exists(self.directory)

    def make_sure_path_exists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def get(self, path):
        try:
            with open(self.directory+path,'r') as data:
                return data.read()
        except IOError as e:
            if e.errno == errno.ENOENT:
                raise KeyError('{}: {}'.format(path,str(e)))

    def put(self, path, data):
        try:
            with open(self.directory+path,'w') as f:
                f.write(data)
        except IOError as exception:
            if exception.errno == errno.ENOENT:
                directory_paths = path.split('/')[:-1]
                for i in range(len(directory_paths)+1):
                    new_path = '/'.join(directory_paths[:i])
                    self.make_sure_path_exists(self.directory+'/'+new_path)
                self.save(path,data)
        

    def delete(self, path):
        os.remove(self.directory+path)

    def exists(self, path):
        if os.path.isfile(self.directory+path): 
            try: 
                x = open(self.directory+path,'r')
                return True
            except IOError:
                return False
        else:
            return False

    def list(self, path):
        for x in os.listdir(self.directory+path):
            yield x
