#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django IBAN Field
~~~~~~~~~~~~~~~~~

:copyright: Copyright 2019-2020 by the Ihor Nahuliak, see AUTHORS.
:license: MIT License, see LICENSE for details.
"""
import os
import sys
from shutil import rmtree

try:
    from setuptools import setup, find_packages, Command
    have_setuptools = True
except ImportError:
    from distutils.core import setup

    def find_packages(*args, **kwargs):
        return [
            'django_iban_field',
        ]

    have_setuptools = False


__author__ = 'Ihor Nahuliak'
__author_email__ = 'ihor.nahuliak@gmail.com'
__url__ = 'https://github.com/ihor-nahuliak/django-iban-field'
__license__ = 'MIT'
__version__ = '0.0.1'

__python_requires__ = [
    '>=3.6',
    '<=3.7',
]
__install_requires__ = [
    'django>=2.2.4',
    'django-localflavor>=2.2',
    'django-middleware-global-request>=0.1.2',
]
__extras_requires__ = {
    'dev': [
        'setuptools',
        'twine',
        'flake8>=3.7.8',
        'python-coveralls>=2.9.3',
    ],
}


ROOT = os.path.abspath(os.path.dirname(__file__))


# Note: To use the 'upload' functionality of this file, you must:
# $ pip install twine --dev
if have_setuptools:

    class UploadCommand(Command):
        """Support of `setup.py upload`."""

        description = 'Build and publish the package.'
        user_options = []

        @staticmethod
        def status(s):
            # print in bold font
            print('\033[1m{0}\033[0m'.format(s))

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            try:
                self.status('Removing previous builds…')
                rmtree(os.path.join(ROOT, 'dist'))
            except OSError:
                pass

            self.status('Building Source and Wheel (universal) distribution…')
            os.system('{0} setup.py sdist bdist_wheel '
                      '--universal'.format(sys.executable))

            self.status('Uploading the package to PyPI via Twine…')
            os.system('twine upload dist/*')

            # self.status('Pushing git tags…')
            # os.system('git tag v{0}'.format(__version__))
            # os.system('git push --tags')

            sys.exit()


    cmdclass = {'upload': UploadCommand}

else:
    cmdclass = None


setup(
    name='django-iban-field',
    version=__version__,
    description=__doc__,
    # long_description=__doc__,
    # long_description_content_type='text/plain',
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    packages=find_packages(exclude=['tests']),
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    python_requires=', '.join(__python_requires__),
    install_requires=__install_requires__,
    extras_require=__extras_requires__,
    license=__license__,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 1 - Planning',
    ],
    # $ setup.py publish support.
    cmdclass=cmdclass,
)
