# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

long_desc = '''
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.
'''

extras_require = {
    'test': [
        'pytest',
    ],
    'lint': [
        'flake8',
        'mypy',
        'types-setuptools',
        'docutils-stubs',
    ],
}


def get_version():
    """Get version number of the package from version.py without importing core module."""
    package_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(package_dir, 'sphinxcontrib/jsmath/version.py')

    namespace = {}
    with open(version_file, 'rt') as f:
        exec(f.read(), namespace)

    return namespace['__version__']


setup(
    name='sphinxcontrib-jsmath',
    version=get_version(),
    url='http://sphinx-doc.org/',
    download_url='https://pypi.org/project/sphinxcontrib-jsmath/',
    license='BSD',
    author='Georg Brandl',
    author_email='georg@python.org',
    description='A sphinx extension which renders display math in HTML via JavaScript',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    platforms='any',
    python_requires=">=3.5",
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    extras_require=extras_require,
    namespace_packages=['sphinxcontrib'],
)
