#Test Suite or Batch Testing
'''
import unittest
from UnitTest_2.test_case_11 import Testing1
from UnitTest_2.test_case_12 import Testing2

#GET ALL TESTS TESTING AND TESTING
tc1=unittest.TestLoader().loadTestsFromTestCase(Testing1.test_method_1())
tc2=unittest.TestLoader().loadTestsFromTestCase(Testing2)

#CREATE A TEST SUITE TO COMBINE TESTING1 AND TESTING2
smoke_test=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(smoke_test)
'''

'''
import unittest
from UnitTest_2.test_case_11 import Testing1
from UnitTest_2.test_case_12 import Testing2

#GET ALL TESTS TESTING AND TESTING
tc1=unittest.TestLoader().loadTestsFromTestCase(Testing1)
tc2=unittest.TestLoader().loadTestsFromTestCase(Testing2)

#CREATE A TEST SUITE TO COMBINE TESTING1 AND TESTING2
suite = unittest.TestSuite()
suite.addTest(Testing1("test_method_1"))
runner = unittest.TextTestRunner()
runner.run(suite)
'''

'''
import unittest
from UnitTest_2.test_case_11 import Testing1
from UnitTest_2.test_case_12 import Testing2

#GET ALL TESTS TESTING AND TESTING
tc1=unittest.TestLoader().loadTestsFromTestCase(Testing1)
tc2=unittest.TestLoader().loadTestsFromTestCase(Testing2)

#CREATE A TEST SUITE TO COMBINE TESTING1 AND TESTING2
suite = unittest.TestSuite()
suite.addTest(Testing1("test_method_1"))
suite.addTest(Testing2("test_method_3"))
runner = unittest.TextTestRunner()
runner.run(suite)
'''

'''
import unittest
from UnitTest_2.test_case_11 import Testing1
from UnitTest_2.test_case_12 import Testing2

#GET ALL TESTS TESTING AND TESTING
tc1=unittest.TestLoader().loadTestsFromTestCase(Testing1)
tc2=unittest.TestLoader().loadTestsFromTestCase(Testing2)

#CREATE A TEST SUITE TO COMBINE TESTING1 AND TESTING2
suite = unittest.TestSuite()
suite.addTest(Testing1("test_method_1"))
suite.addTest(Testing1("test_method_2"))
suite.addTest(Testing2("test_method_3"))
runner = unittest.TextTestRunner()
runner.run(suite)
'''

