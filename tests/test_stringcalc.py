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
        self.assertEqual(329,result)

        #Test any amount of numbers
        result = self.StringCal.add("1,5,6,7,8,9,10,44,50,31,22,1,10,20,30,40,50,60,70,80,90,21,76")
        self.assertEqual(741,result)

    def test_string_non_numbers_raises_error(self): #If string contains characters
        with self.assertRaises(ValueError) as context:
            self.StringCal.add("h,j,k,l")
        self.assertEqual("Input string contains non-numeric data.", str(context.exception))
    
    def test_handle_newline_retrun_sum(self): #Handle new lines between numbers
        result = self.StringCal.add("1\n2,3")
        self.assertEqual(6,result)

    def test_support_diff_delimiter_return_sum(self):
        result = self.StringCal.add("//;\n1;2")
        self.assertEqual(3,result)
    
    def test_negative_numbers_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.StringCal.add("-1,-2,-3")
        self.assertEqual("Negative numbers not allowed.-1,-2,-3", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.StringCal.add("10,20,-1,5,-10,7,-20,-3,9,-1,2")
        self.assertEqual("Negative numbers not allowed.-1,-10,-20,-3,-1", str(context.exception))
    
    def test_number_greater_than_thousand_returns_result(self):
        result = self.StringCal.add("2,1000")
        self.assertEqual(2,result)