__author__ = 'palash'
import subprocess
import unittest


class TestNumericOperators(unittest.TestCase):

        def __init__(self, testname, router1):
            super(TestNumericOperators, self).__init__(testname)
            self.router = router1

        def test_is_lt_passed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "is-lt.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_is_lt_failed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_2", "-t", self.router, "is-lt.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_is_lt_error(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "is-lt_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)

        def test_is_gt_passed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_2", "-t", self.router, "is-gt.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_is_gt_failed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "is-gt.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_is_gt_error(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_2", "-t", self.router, "is-gt_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)

        def test_in_range_passed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "in-range.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_in_range_failed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_2", "-t", self.router, "in-range.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_in_range_error(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "in-range_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)

        def test_not_range_passed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_2", "-t", self.router, "not-range.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_not_range_failed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "not-range.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_not_range_error(self):
            cmd = ["jsnap", "--check", "chassis_fpc_2,chassis_fpc_1", "-t", self.router, "not-range_error.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("Invalid expression"), -1)


if __name__ == '__main__':

        router = "10.216.193.114"
        suite = unittest.TestSuite()
        suite.addTest(TestNumericOperators("test_is_lt_passed", router))
        suite.addTest(TestNumericOperators("test_is_lt_failed", router))
        suite.addTest(TestNumericOperators("test_is_lt_error", router))
        suite.addTest(TestNumericOperators("test_is_gt_passed", router))
        suite.addTest(TestNumericOperators("test_is_gt_failed", router))
        suite.addTest(TestNumericOperators("test_is_gt_error", router))
        suite.addTest(TestNumericOperators("test_in_range_passed", router))
        suite.addTest(TestNumericOperators("test_in_range_failed", router))
        suite.addTest(TestNumericOperators("test_in_range_error", router))
        suite.addTest(TestNumericOperators("test_not_range_passed", router))
        suite.addTest(TestNumericOperators("test_not_range_failed", router))
        suite.addTest(TestNumericOperators("test_not_range_error", router))
        unittest.TextTestRunner().run(suite)
