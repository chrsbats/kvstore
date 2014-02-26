from __future__ import absolute_import
from .core import create, register_adapter
from .fs import FileSystemAdapter
from .s3 import S3Adapter

register_adapter(FileSystemAdapter, 'file')
register_adapter(S3Adapter, 's3')
