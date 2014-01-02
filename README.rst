=====
Store
=====

A simple, persistent key / value data store with multiple back-end adapters.


Example
=======

::

    >>> from __future__ import print_function
    >>> from store import create
    >>> store = create('file://./test_data')
    >>> store.put('test_data.txt', 'Raw data goes in here')
    >>> print(list(store.list('/')))
    ['test_data.txt']
    >>> store.exists('test_data.txt')
    True
    >>> print(store.get('test_data.txt'))
    Raw data goes in here
    >>> store.delete('test_data.txt')
    >>> store.exists('test_data.txt')
    False


Adapters
========

* file system - file://
* S3 - s3://

