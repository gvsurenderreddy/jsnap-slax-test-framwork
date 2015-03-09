import subprocess
import unittest
import runpy
import mock
import sys
import pxssh
class SnapTest(unittest.TestCase):
    def __init__(self,testName, snapname,router,conf_file):
        super(SnapTest, self).__init__(testName)
        self.snapname=snapname
        self.router=router
        self.conf_file= conf_file


    def test_snap_connectivity(self):
        #cmd = sys.arg[0]
        pp = subprocess.Popen(["jsnap", "--snap", self.snapname, "-l", "regress", "-t",self.router, "-p", "MaRtInI", self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        self.assertTrue(out.find("CONNECTED"))


    def test_snap_conf_file_missing(self):
        pp = subprocess.Popen(["jsnap", "--snap", self.snapname, "-l", "regress", "-t", self.router, "-p", "MaRtInI"], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("Configuration file (last parameter) appears to be missing")
        self.assertEqual(pos,0)


    def test_snap_snap_file_missing(self):
        pp = subprocess.Popen(["jsnap", "--snap", "-l", "regress", "-t", self.router, "-p", "MaRtInI", self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("Snapshot name option missing")
        self.assertEqual(pos,0)


    def test_snap_router_missing(self):
        pp = subprocess.Popen(["jsnap", "--snap", self.snapname, "-l", "regress", "-p", "MaRtInI", self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("You must specify the '-t <target>' option")
        self.assertEqual(pos,0)

class SnapCheckTest(unittest.TestCase):
    def __init__(self,testName, snapname,router,conf_file):
        super(SnapCheckTest, self).__init__(testName)
        self.snapname=snapname
        self.router=router
        self.conf_file= conf_file


    def test_snapcheck_connectivity(self):
        #cmd = sys.arg[0]
        pp = subprocess.Popen(["jsnap", "--snapcheck", self.snapname, "-l", "regress", "-t",self.router, "-p", "MaRtInI", self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        self.assertTrue(out.find("CONNECTED"))


    def test_snapcheck_conf_file_missing(self):
        pp = subprocess.Popen(["jsnap", "--snapcheck", self.snapname, "-l", "regress", "-t", self.router, "-p", "MaRtInI"], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("Configuration file (last parameter) appears to be missing")
        self.assertEqual(pos,0)


    def test_snapcheck_snap_file_missing(self):
        pp = subprocess.Popen(["jsnap", "--snapcheck", "-l", "regress", "-t", self.router, "-p", "MaRtInI", self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("Snapshot name option missing")
        self.assertEqual(pos,0)


    def test_snapcheck_router_missing(self):
        pp = subprocess.Popen(["jsnap", "--snapcheck", self.snapname, "-l", "regress", "-p", "MaRtInI", self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("You must specify the '-t <target>' option")
        self.assertEqual(pos,0)

class ComparisonTest(unittest.TestCase):
    def __init__(self,testName, snapname1,snapname2,router,conf_file):
        super(ComparisonTest, self).__init__(testName)
        self.snapname1=snapname1
        self.snapname2=snapname2
        self.router=router
        self.conf_file= conf_file
        self.snapnames = self.snapname1+','+ self.snapname2


    def test_check_conf_file_missing(self):
        pp = subprocess.Popen(["jsnap", "--check", self.snapnames,  "-t", self.router], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("Configuration file (last parameter) appears to be missing")
        self.assertEqual(pos,0)


    def test_check_snap_file_missing(self):
        pp = subprocess.Popen(["jsnap", "--check",self.snapname1, "-t", self.router,  self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("A snapshot name is missing from the command-line.")
        self.assertEqual(pos,0)


    def test_check_router_missing(self):
        pp = subprocess.Popen(["jsnap", "--snap",  self.snapname1,self.snapname2, self.conf_file], stdout=subprocess.PIPE, 	stderr=subprocess.STDOUT, universal_newlines=True)
        out, err = pp.communicate()
        #print(out)
        pos = out.find("You must specify the '-t <target>' option")
        self.assertEqual(pos,0)


snapname1 = "sys1"
snapname2 = "sys2"
router =  "10.216.193.114"
conf_file = "system.conf"
suite = unittest.TestSuite()
suite.addTest(SnapTest("test_snap_connectivity", snapname1,router,conf_file))
suite.addTest(SnapTest("test_snap_conf_file_missing",snapname1,router,conf_file))
suite.addTest(SnapTest("test_snap_snap_file_missing",snapname1,router,conf_file))
suite.addTest(SnapTest("test_snap_router_missing",snapname1,router,conf_file))
suite.addTest(SnapCheckTest("test_snapcheck_connectivity", snapname1,router,conf_file))
suite.addTest(SnapCheckTest("test_snapcheck_conf_file_missing",snapname1,router,conf_file))
suite.addTest(SnapCheckTest("test_snapcheck_snap_file_missing",snapname1,router,conf_file))
suite.addTest(SnapCheckTest("test_snapcheck_router_missing",snapname1,router,conf_file))
suite.addTest(ComparisonTest("test_check_conf_file_missing",snapname1,snapname2,router,conf_file))
suite.addTest(ComparisonTest("test_check_snap_file_missing",snapname1,snapname2,router,conf_file))
suite.addTest(ComparisonTest("test_check_router_missing",snapname1,snapname2,router,conf_file))
unittest.TextTestRunner().run(suite)

