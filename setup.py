from distutils.core import setup

setup(
    name='kvstore',
    version='0.4',
    author='C Bates',
    author_email='chrsbats@gmail.com',
    packages=['kvstore'],
    scripts=[],
    url='https://github.com/chrsbats/kvstore',
    license='LICENSE.TXT',
    description='Key value store with Filesystem and S3 backends',
    long_description='Key value store with Filesystem and S3 backends',
    install_requires=[
        "boto==2.15.0",
    ],
)
