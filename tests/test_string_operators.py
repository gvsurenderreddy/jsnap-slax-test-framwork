__author__ = 'palash'
import subprocess
import unittest


class TestStringOperators(unittest.TestCase):

        def __init__(self, testname, router1):
            super(TestStringOperators, self).__init__(testname)
            self.router = router1

        def test_contains_passed(self):
            cmd = ["jsnap", "--check", "version_check_2,version_check_1", "-t", self.router, "contains.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_contains_failed(self):
            cmd = ["jsnap", "--check", "version_check_1,version_check_2", "-t", self.router, "contains.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_contains_error(self):
            cmd = ["jsnap", "--check", "version_check_2,version_check_1", "-t", self.router, "contains_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)

        def test_is_in_passed(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "is-in.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_is_in_failed(self):
            cmd = ["jsnap", "--check", "interf2,interf", "-t", self.router, "is-in.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_not_in_passed(self):
            cmd = ["jsnap", "--check", "interf2,interf", "-t", self.router, "not-in.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_not_in_failed(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "not-in.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_is_in_error(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "is-in_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid number of arguments"), -1)

        def test_not_in_error(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "not-in_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid number of arguments"), -1)


router = "10.216.193.114"
suite = unittest.TestSuite()
suite.addTest(TestStringOperators("test_contains_passed", router))
suite.addTest(TestStringOperators("test_contains_failed", router))
suite.addTest(TestStringOperators("test_contains_error", router))
suite.addTest(TestStringOperators("test_is_in_passed", router))
suite.addTest(TestStringOperators("test_is_in_failed", router))
suite.addTest(TestStringOperators("test_not_in_passed", router))
suite.addTest(TestStringOperators("test_not_in_failed", router))
suite.addTest(TestStringOperators("test_is_in_error", router))
suite.addTest(TestStringOperators("test_not_in_error", router))
unittest.TextTestRunner().run(suite)
