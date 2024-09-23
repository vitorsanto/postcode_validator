import time
import random
import string
import unittest
from postcode_validator.postcode_service_builder import PostcodeServiceBuilder


class PerformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = PostcodeServiceBuilder.build("UK")

    def test_time_to_million_validation(self):
        start_time = time.time()
        for _ in range(1000000):
            postcode = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=8)
            )
            self.service.validate(postcode)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"Execution time for 1000000 postcode validations: {execution_time} seconds"
        )

    def test_validations_per_minute(self):
        start_time = time.time()
        count = 0
        while time.time() - start_time < 60:
            postcode = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=8)
            )
            self.service.validate(postcode)
            count += 1
        print(f"Number of postcode validations in 1 minute: {count}")

    def test_validations_per_second(self):
        start_time = time.time()
        count = 0
        while time.time() - start_time < 1:
            postcode = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=8)
            )
            self.service.validate(postcode)
            count += 1
        print(f"Number of postcode validations in 1 second: {count}")
