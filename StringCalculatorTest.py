from StringCalculator import add

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
  def test_custom_delimiter_semicolon(self):
    self.assertEqual(add("//;\n1;2"), 3)
  def test_negative_raise_exception(self):
    with self.assertRaises(ValueError) as context:
      add("1,-2,3,-4")
    self.assertIn("negatives not allowed", str(context.exception))
    self.assertIn("-2", str(context.exception))
    self.assertIn("-4", str(context.exception))
  def test_numbers_ignoring_greater_than_1000(self):
    self.assertEqual(add("2,1001"), 2)
    self.assertEqual(add("1000,1001,2"), 1002)

  def test_multi_character_delimiter(self):
    self.assertEqual(add("//[***]\n1***2***3"), 6)
    self.assertEqual(add("//[%%]\n4%%5%%6"), 15)
