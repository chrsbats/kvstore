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
    >>> store.put('/my_data/some_text', 'Raw data goes in here')
    >>> print(list(store.list('/my_data')))
    ['/my_data/some_text']
    >>> store.exists('/my_data/some_text')
    True
    >>> print(store.get('/my_data/some_text'))
    Raw data goes in here
    >>> store.delete('/my_data/some_text')
    >>> store.exists('/my_data/some_text')
    False


Adapters
========

* file system - file://
* S3 - s3://

