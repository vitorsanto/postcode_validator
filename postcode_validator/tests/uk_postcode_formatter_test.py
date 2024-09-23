import unittest
from postcode_validator.formatters.uk_postcode_formatter import UKPostcodeFormatter


class TestUKPostcodeFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = UKPostcodeFormatter()

    def test_format(self):
        # Test case 1: Valid postcode with space
        postcode = "SW1A 1AA"
        expected_result = "SW1A 1AA"
        self.assertEqual(self.formatter.format(postcode), expected_result)

        # Test case 2: Valid postcode without space
        postcode = "SW1A1AA"
        expected_result = "SW1A 1AA"
        self.assertEqual(self.formatter.format(postcode), expected_result)

        # Test case 3: Valid postcode with lowercase letters
        postcode = "sw1a 1aa"
        expected_result = "SW1A 1AA"
        self.assertEqual(self.formatter.format(postcode), expected_result)

        # Test case 4: Valid postcode with leading/trailing spaces
        postcode = "  SW1A 1AA  "
        expected_result = "SW1A 1AA"
        self.assertEqual(self.formatter.format(postcode), expected_result)

        # Test case 5: Valid postcode with special characters
        postcode = "-- -SW1A@1AA+++"
        expected_result = "SW1A 1AA"
        self.assertEqual(self.formatter.format(postcode), expected_result)

        # Test case 6: Invalid postcode with wrong format
        postcode = "SW1A1A"
        expected_result = "SW1 A1A"
        self.assertEqual(self.formatter.format(postcode), expected_result)

        # Test case 7: Invalid input type
        postcode = 123445
        expected_result = "SW1 A1A"
        self.assertRaises(TypeError, self.formatter.format, postcode)
