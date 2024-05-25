#Test module - String Calculator
import unittest

from stringcalc.stringcalc import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.StringCal = StringCalculator()

    def test_empty_string_returns_zero(self):
        result = self.StringCal.add("")
        self.assertEqual(0, result)
    
    def test_string_number_returns_sum(self):
        result = self.StringCal.add("1")
        self.assertEqual(1,result)
    