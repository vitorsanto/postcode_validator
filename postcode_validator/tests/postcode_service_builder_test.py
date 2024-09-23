import unittest
from postcode_validator.enums import PostcodeType
from postcode_validator.services.postcode_service_interface import (
    PostcodeServiceInterface,
)
from postcode_validator.services.uk_postcode_service import UKPostcodeService
from postcode_validator.postcode_service_builder import PostcodeServiceBuilder
from postcode_validator.exceptions import InvalidPostcodeException


class TestPostcodeServiceBuilder(unittest.TestCase):
    def test_build_uk_postcode_service(self):

        postcode_type = PostcodeType.UK
        expected_service = UKPostcodeService()

        service = PostcodeServiceBuilder.build(postcode_type)

        self.assertIsInstance(service, PostcodeServiceInterface)
        self.assertIsInstance(service, UKPostcodeService)
        self.assertEqual(service.__class__, expected_service.__class__)

    def test_build_invalid_postcode_type(self):

        postcode_type = "InvalidType"

        with self.assertRaises(InvalidPostcodeException):
            PostcodeServiceBuilder.build(postcode_type)

    def test_build_with_invalid_params(self):

        postcode_type = []

        with self.assertRaises(TypeError):
            PostcodeServiceBuilder.build(postcode_type)

    def test_build_with_cache(self):

        postcode_type = PostcodeType.UK
        cache = set(["AB12 3CD", "EF45 6GH"])
        expected_service = UKPostcodeService(cache=cache)

        service = PostcodeServiceBuilder.build(postcode_type, cache)

        self.assertIsInstance(service, PostcodeServiceInterface)
        self.assertIsInstance(service, UKPostcodeService)
        self.assertEqual(service.__class__, expected_service.__class__)
        self.assertEqual(service._cache, cache)
