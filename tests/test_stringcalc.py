#Test module - String Calculator
import unittest

from stringcalc.stringcalc import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.StringCal = StringCalculator()

    def test_empty_string_returns_zero(self): #Test empty string
        result = self.StringCal.add("")
        self.assertEqual(0, result)
    
    def test_string_numbers_returns_sum(self): #Test digit
        result = self.StringCal.add("1")
        self.assertEqual(1,result)
        
        #Test single digits
        result = self.StringCal.add("1,5")
        self.assertEqual(6,result)

        #Test 2/3/4 digit numbers
        result = self.StringCal.add("3000,40,289")
        self.assertEqual(3329,result)

        #Test any amount of numbers
        result = self.StringCal.add("1,5,6,7,8,9,10,44,50,31,22,1,10,20,30,40,50,60,70,80,90,21,76")
        self.assertEqual(741,result)

    def test_string_non_numbers_raises_error(self): #If string contains characters
        self.assertRaises(ValueError, self.StringCal.add, "h,j,k,l")