import unittest
from postcode_validator.validators.uk_postcode_validator import UKPostcodeValidator


class TestUKPostcodeValidator(unittest.TestCase):
    def setUp(self):
        self.validator = UKPostcodeValidator()

    def test_valid_postcodes(self):
        valid_postcodes = [
            "SW1A 1AA",
            "EC1A 1BB",
            "W1A 0AX",
            "M1 1AE",
            "B33 8TH",
            "CR2 6XH",
            "DN55 1PT",
            "KY11 9YU",
            "AB10 1XG",
            "ZE1 0AE",
        ]

        for postcode in valid_postcodes:
            self.assertTrue(self.validator.is_valid(postcode))

    def test_invalid_postcodes(self):
        invalid_postcodes = [
            "SW1A 1A",
            "EC1A 1B",
            "W1A 0A",
            "M1 1A",
            "B33 8T",
            "CR2 6X",
            "DN55 1P",
            "KY11 9Y",
            "AB10 1X",
            "ZE1 0A",
            "12345",
            "ABCDEF",
            "SW1A 1AAA",
            "EC1A 1BBB",
            "W1A 0AXX",
            "M1 1AEE",
            "B33 8THH",
            "CR2 6XHH",
            "DN55 1PTT",
            "KY11 9YUU",
            "AB10 1XGG",
            "AB101XGG",
            "ZE1 0AEE",
        ]

        for postcode in invalid_postcodes:
            self.assertFalse(self.validator.is_valid(postcode))

    def test_invalid_input_type(self):
        invalid_postcodes = [
            12345,
            123.45,
            True,
            False,
            None,
            ["SW1A 1AA"],
            {"postcode": "SW1A 1AA"},
        ]

        for postcode in invalid_postcodes:
            self.assertRaises(TypeError, self.validator.is_valid, postcode)
