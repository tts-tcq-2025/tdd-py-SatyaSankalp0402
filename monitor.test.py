import unittest
from String_Calculator import add

class StringCalculatorTests(unittest.TestCase):
  def test_empty_string_returns_zero(self):
    self.assertEqual(add(""),0)
  def test_single_number_returns_its_value(self):
    self.assertEqual(add("1"), 1)
  def test_two_numbers_comma_separated_returns_sum(self):
    self.assertEqual(add("1,2"), 3)
  def test_multiple_numbers_returns_sum(self):
    self.assertEqual(add("1,2,3"), 6)
  def test_newline_as_separator(self):
    self.assertEqual(add("1\n2,3"), 6)
     
if __name__ == "__main__":
  unittest.main()
