=====
KV Store
=====

An extremely simple, persistent key / value data store with support for various data stores through adaptors.

KV Store currently supports filesystems and S3.  More to come.


Requirements
============

python 2.7
boto 2.15.0


Example
=======

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

 * file system
    ```
    store = kvstore.create('file://'+relative_directory)
    ```

 * S3
    ```
    os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
    store = kvstore.create('s3://'+s3_bucket_name)
    ```



Motivation
==========

KV Store attempts to be efficient with regards to calls to s3, unlike some other s3 wrappers that sometimes use multiple calls for simple operations in order acheive a broader feature set (which can make s3 expensive in terms of $ when making many operations).

The filesystem adapter is also very useful when mocking out an s3 interface for testing locally.

Authors
=======

KV Store was created by [Christopher Bates](https://github.com/chrsbats) and [Adam Griffiths](https://github.com/adamlwgriffiths).

