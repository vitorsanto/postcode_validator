import unittest
from postcode_validator.services.uk_postcode_service import UKPostcodeService


class TestUKPostcodeService(unittest.TestCase):
    def setUp(self):
        self.postcode_service = UKPostcodeService()

    def test_validate_valid_postcode(self):
        raw_postcode = "SW1A 1AA"
        result = self.postcode_service.validate(raw_postcode)
        self.assertTrue(result["valid"])
        self.assertEqual(result["postcode"], "SW1A 1AA")

    def test_validate_invalid_postcode(self):
        raw_postcode = "ABC123"
        result = self.postcode_service.validate(raw_postcode)
        self.assertFalse(result["valid"])
        self.assertEqual(result["postcode"], "ABC123")

    def test_validate_postcode_with_whitespace(self):
        raw_postcode = "   EC1A 1BB   "
        result = self.postcode_service.validate(raw_postcode)
        self.assertTrue(result["valid"])
        self.assertEqual(result["postcode"], "EC1A 1BB")

    def test_validate_postcode_with_lowercase_letters(self):
        raw_postcode = "w1a 1aa"
        result = self.postcode_service.validate(raw_postcode)
        self.assertTrue(result["valid"])
        self.assertEqual(result["postcode"], "W1A 1AA")

    def test_validate_postcode_with_invalid_format(self):
        raw_postcode = "SW1A1AA"
        result = self.postcode_service.validate(raw_postcode)
        self.assertTrue(result["valid"])
        self.assertEqual(result["postcode"], "SW1A 1AA")

    def test_validate_postcode_with_cache(self):
        raw_postcode = "SW1A 1AA"
        postcode_service = UKPostcodeService(cache=set())
        postcode_service._cache.add(raw_postcode)
        result = postcode_service.validate(raw_postcode)
        self.assertTrue(result["valid"])
        self.assertEqual(result["postcode"], "SW1A 1AA")

    def test_validate_postcode_not_in_cache(self):
        raw_postcode = "SW1A 1AA"
        result = self.postcode_service.validate(raw_postcode)
        self.assertTrue(result["valid"])
        self.assertEqual(result["postcode"], "SW1A 1AA")

    def test_validate_postcode_with_invalid_input_type(self):
        raw_postcode = 12345
        with self.assertRaises(TypeError):
            self.postcode_service.validate(raw_postcode)

    def test_build_postcode_service_with_invalid_cache(self):
        raw_postcode = "SW1A 1AA"
        service = UKPostcodeService(cache=123)
        self.assertEqual(service._cache, 123)

        with self.assertRaises(TypeError):
            service.validate(raw_postcode)
