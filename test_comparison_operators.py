__author__ = 'palash'
import subprocess
import unittest


class TestComparisionOperators(unittest.TestCase):

        def __init__(self, testname, router1):
            super(TestComparisionOperators, self).__init__(testname)
            self.router = router1

        def test_no_diff_passed(self):
            cmd = ["jsnap", "--check", "interface_3,interface_4", "-t", self.router, "no-diff.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_no_diff_failed(self):
            cmd = ["jsnap", "--check", "interface,interface2", "-t", self.router, "no-diff.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_no_diff_skipped(self):
            cmd = ["jsnap", "--check", "interface,interface", "-t", self.router, "no-diff.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("SKIPPING"), -1)

        def test_list_not_less_passed(self):
            cmd = ["jsnap", "--check", "interface,interface2", "-t", self.router, "list-not-less.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_list_not_less_failed(self):
            cmd = ["jsnap", "--check", "interface2,interface", "-t", self.router, "list-not-less.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_list_not_less_skipped(self):
            cmd = ["jsnap", "--check", "interface,interface", "-t", self.router, "list-not-less.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("SKIPPING"), -1)


        def test_list_not_more_passed(self):
            cmd = ["jsnap", "--check", "interface2,interface", "-t", self.router, "list-not-more.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_list_not_more_failed(self):
            cmd = ["jsnap", "--check", "interface,interface2", "-t", self.router, "list-not-more.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_list_not_more_skipped(self):
            cmd = ["jsnap", "--check", "interface,interface", "-t", self.router, "list-not-more.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("SKIPPING"), -1)


        def test_delta_passed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_3", "-t", self.router, "delta.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST PASSED"), -1)

        def test_delta_failed(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_2", "-t", self.router, "delta.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("TEST FAILED"), -1)

        def test_delta_skipped(self):
            cmd = ["jsnap", "--check", "chassis_fpc_1,chassis_fpc_1", "-t", self.router, "delta.conf"]
            pp = subprocess.Popen(cmd, stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
            out, err = pp.communicate()
            self.assertNotEqual(out.find("SKIPPING"), -1)





if __name__ == '__main__':

        router = "10.216.193.114"
        suite = unittest.TestSuite()
        suite.addTest(TestComparisionOperators("test_no_diff_passed", router))
        suite.addTest(TestComparisionOperators("test_no_diff_failed", router))
        suite.addTest(TestComparisionOperators("test_no_diff_skipped", router))
        suite.addTest(TestComparisionOperators("test_list_not_less_passed", router))
        suite.addTest(TestComparisionOperators("test_list_not_less_failed", router))
        suite.addTest(TestComparisionOperators("test_list_not_less_skipped", router))
        suite.addTest(TestComparisionOperators("test_list_not_more_passed", router))
        suite.addTest(TestComparisionOperators("test_list_not_more_failed", router))
        suite.addTest(TestComparisionOperators("test_list_not_more_skipped", router))
        suite.addTest(TestComparisionOperators("test_delta_passed", router))
        suite.addTest(TestComparisionOperators("test_delta_failed", router))
        suite.addTest(TestComparisionOperators("test_delta_skipped", router))
        unittest.TextTestRunner().run(suite)
