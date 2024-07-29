Release 2.0.0 (unreleased)
==========================

* Adopt Ruff
* Tighten MyPy settings
* Update GitHub actions versions
* Remove Sphinx as a required dependency, as circular dependencies may cause
  failure with package managers that expect a directed acyclic graph (DAG)
  of dependencies.
* Drop support for Python 3.5, 3.6, 3.7, and 3.8
* Raise minimum required Sphinx version to 5.0

Release 1.0.1 (2019-01-22)
==========================

* sphinx-doc/sphinx#5966: jsmath has not been loaded on incremental build

Release 1.0.0 (2019-01-13)
==========================

* Initial release (copied from sphinx package)
