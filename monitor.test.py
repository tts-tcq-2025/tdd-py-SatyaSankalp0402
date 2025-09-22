import unittest
from String_Calculator import add

class StringCalculatorTests(unittest.TestCase):
  def test_empty_string_returns_zero(self):
    self.assertEqual(add(""),0)
  def test_single_number_returns_its_value(self):
    self.assertEqual(add("1"), 1)

if __name__ == "__main__":
  unittest.main()
