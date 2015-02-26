__author__ = 'palash'
import subprocess
import unittest


class TestNumericStringOperators(unittest.TestCase):

        def __init__(self, testname, router1):
            super(TestNumericStringOperators, self).__init__(testname)
            self.router = router1

        def test_all_same_passed(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "all-same.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_all_same_failed(self):
            cmd = ["jsnap", "--check", "interf2,interf", "-t", self.router, "all-same.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_all_same_equal_passed(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "all-same_equal.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_all_same_equal_failed(self):
            cmd = ["jsnap", "--check", "interf2,interf", "-t", self.router, "all-same_equal.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_is_equal_passed(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "is-equal.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_is_equal_failed(self):
            cmd = ["jsnap", "--check", "interf2,interf", "-t", self.router, "is-equal.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_is_equal_error(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "is-equal_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)

        def test_not_equal_passed(self):
            cmd = ["jsnap", "--check", "interf2,interf", "-t", self.router, "not-equal.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_not_equal_failed(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "not-equal.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_not_equal_error(self):
            cmd = ["jsnap", "--check", "interf,interf2", "-t", self.router, "not-equal_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)



if __name__ == '__main__':

        router = "10.216.193.114"
        suite = unittest.TestSuite()
        suite.addTest(TestNumericStringOperators("test_all_same_passed", router))
        suite.addTest(TestNumericStringOperators("test_all_same_failed", router))
        suite.addTest(TestNumericStringOperators("test_all_same_equal_passed", router))
        suite.addTest(TestNumericStringOperators("test_all_same_equal_failed", router))
        suite.addTest(TestNumericStringOperators("test_is_equal_passed", router))
        suite.addTest(TestNumericStringOperators("test_is_equal_failed", router))
        suite.addTest(TestNumericStringOperators("test_is_equal_error", router))
        suite.addTest(TestNumericStringOperators("test_not_equal_passed", router))
        suite.addTest(TestNumericStringOperators("test_not_equal_failed", router))
        suite.addTest(TestNumericStringOperators("test_not_equal_error", router))
        unittest.TextTestRunner().run(suite)
