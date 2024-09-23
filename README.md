# Postcode Validator
This is a Python library designed for validating postcodes, with a focus on UK postcodes. However, it can be easily extended to support other types of postcodes.

The library provides a factory class that builds the appropriate postcode validator based on the given postcode type (e.g., UK). It also offers a simple memory cache mechanism that can be passed as a parameter to the factory class. The cache, which must be a set, is used to check if a postcode is already present. If it is, the postcode is automatically validated.

The validation service will always return a dict with the following keys:

```
{
    "valid": bool (True or False),
    "postcode": str (Formatted postcode if valid and raw postcode otherwise)
}

```

## Usage (Demo)

To see a demo of this library in action, you can use the included docker container. To start it, execute `make start`. To stop it, use `make stop`. You can also run the library tests using the docker container with `make test`. Once the docker container is up and running, you can make a POST request to the following endpoint:

```
curl -X 'POST' \
    'http://localhost:8000/api/v1/postcode/validate' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "postcode": "AA9 9AA",
    "postcode_type": "UK"
}'
```

## Usage (Standalone)

To use the library independently, import the `PostcodeServiceBuilder` class from the `postcode_validator.postcode_service_builder` module and call the `build` method. This will create a service that corresponds to the type of postcode you want to validate:

```python
from postcode_validator.postcode_service_builder import PostcodeServiceBuilder

service = PostcodeServiceBuilder.build("UK")

postcode = "SW1A 1AA"
response = service.validate(postcode)

if response["valid"]:
    print("The postcode is valid.")
else:
    print("The postcode is invalid.")
```

## Interactive Docs

Interactive documentation can be found in:
- http://localhost:8000/docs (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui]))
- http://localhost:8000/redoc  (provided by [ReDoc](https://github.com/Rebilly/ReDoc))

## Performance

Data extracted from the performance test suite of the library:

- Execution time for 1,000,000 postcode validations: 1.66 seconds
- Number of postcode validations in 1 minute: 35,485,747
- Number of postcode validations in 1 second: 592,313

Please note that these results may vary depending on the hardware used.
To execute the performance test, run `make test_performance`.

## Avaliable make commands

### Build the Docker image

To build the Docker image, use the following command:

```
make build
```

### Rebuild the Docker image without cache

To rebuild the Docker image without using the cache, use the following command:

```
make rebuild
```

### Start or run the Docker container

To start or run the Docker container, use the following command:

```
make start
```

### Stop the Docker container

To stop the Docker container, use the following command:

```
make stop
```

### Restart the Docker container

To restart the Docker container, use the following command:

```
make restart
```

### Check the logs of the Docker container

To check the logs of the Docker container, use the following command:

```
make logs
```

### Remove the Docker container

To remove the Docker container, use the following command:

```
make rm
```

### Run tests using the Docker container

To run tests using the Docker container, use the following command:

```
make test
```

### Run performance tests using the Docker container

To run performance tests using the Docker container, use the following command:

```
make test_performance
```

