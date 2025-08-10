# Ice Breaker Application - Development Commands
# 
# This Makefile provides shortcuts for common development tasks.
# Use 'make help' to see all available commands.

.PHONY: help setup install install-dev run test lint format clean docker-build docker-run

# Default target
help:
	@echo "Ice Breaker Application - Available Commands:"
	@echo ""
	@echo "Setup Commands:"
	@echo "  make setup        - Complete project setup (recommended for first time)"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo ""
	@echo "Development Commands:"
	@echo "  make run          - Run the Flask application"
	@echo "  make test         - Run tests with pytest"
	@echo "  make lint         - Run code linting with flake8"
	@echo "  make format       - Format code with black and isort"
	@echo "  make clean        - Clean up temporary files"
	@echo ""
	@echo "Docker Commands:"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run   - Run application in Docker container"
	@echo ""
	@echo "Environment:"
	@echo "  Copy .env.template to .env and add your API keys before running."

# Setup commands
setup:
	@echo "🧊 Setting up Ice Breaker application..."
	python setup.py

install:
	@echo "📦 Installing production dependencies..."
	pip install -r requirements.txt

install-dev: install
	@echo "📦 Installing development dependencies..."
	pip install black isort flake8 pytest pytest-cov mypy

# Development commands
run:
	@echo "🚀 Starting Ice Breaker application..."
	@echo "Application will be available at http://localhost:5000"
	python app.py

test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v

lint:
	@echo "🔍 Running code linting..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

format:
	@echo "✨ Formatting code..."
	black .
	isort .

clean:
	@echo "🧹 Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.log" -delete

# Docker commands (optional - would need Dockerfile)
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t ice-breaker .

docker-run:
	@echo "🐳 Running Docker container..."
	docker run -p 5000:5000 --env-file .env ice-breaker

# Check environment
check-env:
	@echo "🔐 Checking environment setup..."
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found. Run 'make setup' or copy .env.template to .env"; \
		exit 1; \
	fi
	@echo "✅ Environment file found"

# Development workflow
dev: install-dev format lint test
	@echo "✅ Development workflow complete!"

# Production workflow  
prod: install clean test
	@echo "✅ Production workflow complete!"
