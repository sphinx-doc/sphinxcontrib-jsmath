ToDo for releasing
==================

preparation
-----------
1. run ``python setup.py extract_messages``
2. run ``(cd sphinxcontrib/jsmath/locales/; tx push -s)``
3. call for translation

release
-------
1.  check travis-ci testing result
2.  run ``(cd sphinxcontrib/jsmath/locales/; tx pull -a -f)``
3.  run ``python setup.py compile_catalog``
4.  Run ``git add sphinxcontrib``
5.  Run ``git commit -am 'Update message catalogs'``
6.  check release version in ``sphinxcontrib/jsmath/version.py``
7.  Run ``make clean``
8.  build distribtion files: ``python setup.py release sdist bdist_wheel``
9.  make a release: ``twine upload --sign --identity=<your-identify> dist/<new-version-files>``
10. check PyPI page: https://pypi.org/p/sphinxcontrib-jsmath
11. tagging with version name. e.g.: git tag 1.1.0
12. bump version in ``sphinxcontrib/jsmath/version.py``

