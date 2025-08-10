# Contributing to Ice Breaker

Thank you for considering contributing to the Ice Breaker project! This document provides guidelines for contributing to this AI-powered conversation starter application.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information** including:
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Environment details (Python version, OS, etc.)
   - API versions used

### Suggesting Enhancements

1. **Check existing feature requests** to avoid duplicates
2. **Clearly describe the enhancement** with use cases
3. **Explain why this enhancement would be useful** to most users
4. **Provide examples** of how the feature would work

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the coding standards** outlined below
3. **Add tests** for any new functionality
4. **Update documentation** as needed
5. **Ensure all tests pass** before submitting
6. **Write clear commit messages** following conventional commits

## 🏗️ Development Setup

1. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/ice_breaker.git
   cd ice_breaker
   ```

2. **Set up Python environment:**
   ```bash
   # Using Pipenv (recommended)
   pipenv install --dev
   pipenv shell
   
   # Or using pip
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.template .env
   # Edit .env with your API keys
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

## 📝 Coding Standards

### Python Code Style

- **Follow PEP 8** for Python code style
- **Use type hints** where appropriate
- **Write docstrings** for all functions and classes
- **Keep functions small** and focused on a single responsibility
- **Use meaningful variable names**

### Code Formatting

- **Use Black** for code formatting: `black .`
- **Use isort** for import sorting: `isort .`
- **Run flake8** for linting: `flake8 .`

### Documentation

- **Update README.md** if you change functionality
- **Add docstrings** to new functions and classes
- **Include code examples** in docstrings where helpful
- **Update type hints** as needed

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=.

# Run specific test file
python -m pytest tests/test_specific.py
```

### Writing Tests

- **Write tests** for new functionality
- **Follow the existing test structure**
- **Use descriptive test names** that explain what is being tested
- **Mock external API calls** to avoid depending on external services

## 📁 Project Structure

```
ice_breaker/
├── app.py                      # Flask web application
├── ice_breaker.py             # Main application logic
├── output_parsers.py          # Pydantic models
├── agents/                    # AI agents
│   ├── linkedin_lookup_agent.py
│   └── twitter_lookup_agent.py
├── third_parties/            # External API integrations
│   ├── linkedin.py
│   └── twitter.py
├── tools/                    # Utility functions
│   └── tools.py
└── templates/                # HTML templates
    └── index.html
```

## 🔄 Commit Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Example:
```
feat: add support for Instagram profile analysis
fix: handle rate limiting in Twitter API calls
docs: update installation instructions
```

## 🚀 Deployment Considerations

- **Test with mock data** before using live APIs
- **Handle API rate limits** gracefully
- **Validate environment variables** on startup
- **Log errors appropriately** for debugging

## 📋 Code Review Process

1. **All changes** must go through pull requests
2. **At least one approval** required before merging
3. **All tests must pass** in CI/CD
4. **Code style checks** must pass
5. **Documentation** must be updated if needed

## 🌟 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Project documentation

## 📞 Getting Help

- **Create an issue** for bugs or feature requests
- **Join discussions** in the repository discussions tab
- **Reference the original course** by Eden Marco for additional context

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.

---

Thank you for contributing to Ice Breaker! Your efforts help make this project better for everyone. 🙏
