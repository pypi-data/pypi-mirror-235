from setuptools import setup, find_packages
import os

reqs = os.popen('pipreqs requirements.txt').read().splitlines()


setup(
    name='encryption_jsv',
    version='0.0.1',
    packages=find_packages(),
    author='valan',
    author_email='sahayavalanj1@gmail.com',
    description='This (CLI) application is a file encryption tool that provides a simple and secure way to encrypt files using the AES or DES encryption algorithms',
    install_requires=reqs,

entry_points={
    'console_scripts':['encryption_jsv=enc_app.encrypt.py:main']
}
)