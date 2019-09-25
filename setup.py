from setuptools import setup

setup(
    name='snapShotAlayzer30001',
    version='0.1',
    author='rob',
    author_email='notyet@gmail.com',
    description="snapShotAlayzer30001 is a tool to manage EC2 snapshots",
    license='GPLv3+',
    packages=['shotty'],
    url="https://github.com/rlad809118/snapShotAlayzer30001",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
