"""
    pytest config for sphinx extensions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os
import shutil

import pytest

from sphinx.testing.path import path

pytest_plugins = 'sphinx.testing.fixtures'


@pytest.fixture(scope='session')
def rootdir():
    return path(os.path.dirname(__file__)).abspath() / 'roots'


def _initialize_test_directory(session):
    testroot = os.path.join(str(session.config.rootdir), 'tests')
    tempdir = os.path.abspath(os.getenv('SPHINX_TEST_TEMPDIR',
                              os.path.join(testroot, 'build')))
    os.environ['SPHINX_TEST_TEMPDIR'] = tempdir

    print('Temporary files will be placed in %s.' % tempdir)

    if os.path.exists(tempdir):
        shutil.rmtree(tempdir)

    os.makedirs(tempdir)


def pytest_sessionstart(session):
    _initialize_test_directory(session)
