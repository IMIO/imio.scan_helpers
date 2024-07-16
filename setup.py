# setup.py
import os
from setuptools import setup, find_packages


def get_version():
    with open('imio/scan-helpers/version.txt', 'r') as file:
        return file.readline().strip()


setup(
    name='imio.scan-helpers',
    version=get_version(),
    description='Various script files to handle local scan tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Stephan Geulette (IMIO)',
    author_email='support@imio.be',
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/imio.scan-helpers",
        "Source": "https://github.com/IMIO/imio.scan-helpers",
    },
    license='GPL version 3',
    keywords='Scan Windows',
    packages=find_packages(exclude=['ez_setup']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
    ],
    install_requires=[
    ],
)
