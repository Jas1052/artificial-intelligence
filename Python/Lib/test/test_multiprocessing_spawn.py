import unittest
import thelab._test_multiprocessing

thelab._test_multiprocessing.install_tests_in_module_dict(globals(), 'spawn')

if __name__ == '__main__':
    unittest.main()