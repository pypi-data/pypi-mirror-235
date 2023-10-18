from setuptools import setup, find_packages
import os

reqs = os.popen('pipreqs requirements.txt').read().splitlines()

with open('README.md', 'r') as f:
    ld = f.read()

setup(
    name='encryption_jsv',
    version='0.1.2',
    packages=find_packages(),
    author='valan',
    author_email='sahayavalanj1@gmail.com',
    description='This (CLI) application is a file encryption tool that provides a simple and secure way to encrypt files using the AES or DES encryption algorithms',
    long_description=ld,
    long_description_content_type='markdown',
    install_requires=reqs,

    entry_points={
        'console_scripts': ['encryption_jsv=enc_app.encrypt:main']
    }
)
