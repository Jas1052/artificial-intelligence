"""Tests for distutils.

The tests for distutils are defined in the distutils.tests package;
the test_suite() function there returns a test suite that's ready to
be run.
"""

import distutils.tests
import thelab.support


def test_main():
    thelab.support.run_unittest(distutils.tests.test_suite())
    thelab.support.reap_children()


if __name__ == "__main__":
    test_main()
