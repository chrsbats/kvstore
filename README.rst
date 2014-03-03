=====
Store
=====

A simple, persistent key / value data store with support for various data stores through adaptors.

Store currently supports filesystems and S3.


Example
=======

::

    >>> from __future__ import print_function
    >>> import kvstore
    >>> store = kvstore.create('file://./test_data')
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

* file system - file://<directory>
* S3 - s3://<s3_key>:<s3_secret>@<bucket>


Motivation
==========

KVstore attempts to be efficient with in regards to calls to s3, unlike some other s3 wrappers that sometimes use multiple calls for simple operations in order acheive a broader feature set (which can make s3 expensive in terms of $ when making many operations).

The filesystem adapter is useful for mocking out an s3 interface when testing locally.

Authors
=======

Store was created by Christopher Bates (@chrsbats) and cleaned up by Adam Griffiths (@adamlwgriffiths).

