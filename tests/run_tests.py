__author__ = 'palash'
import unittest
import runpy

if __name__ == '__main__':
    runpy.run_module("test_connectivity")
    runpy.run_module("test_string_numeric_operators")
    runpy.run_module("test_comparison_operators")
    runpy.run_module("test_numeric_operators")
    runpy.run_module("test_string_operators")