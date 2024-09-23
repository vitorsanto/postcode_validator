.PHONY: build rebuild start stop logs rm test test_performance restart

# Build the Docker image
build:
	docker-compose build

# Rebuild the Docker image without cache
rebuild:
	docker-compose build --no-cache

# Start or run the Docker container
start:
	docker-compose up -d

# Stop the Docker container
stop:
	docker-compose down

# Restart the Docker container
restart:
	docker-compose down
	docker-compose up -d

# Check the logs of the Docker container
logs:
	docker-compose logs -f

# Remove the Docker container
rm:
	docker-compose down --rmi all

# Run tests using the Docker container
test:
	docker-compose run --rm app python -m unittest discover -s postcode_validator/tests -p '*_test.py'

# Run performance tests using the Docker container
test_performance:
	docker-compose run --rm app python -m unittest discover -s postcode_validator/tests -p 'performance.py'