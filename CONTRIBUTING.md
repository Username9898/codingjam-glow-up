# Contributing to Universal Try-On Platform

We love your input! We want to make contributing to this project as easy and transparent as possible.

## Development Process

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/awesome-feature`)
3. **Make** your changes with clear commit messages
4. **Test** thoroughly (see Testing section)
5. **Submit** a Pull Request with description

## Pull Request Process

- Update README.md with any new features
- Add tests for new functionality
- Ensure CI/CD pipeline passes
- Request review from maintainers
- Squash commits before merge

## Code Standards

### Python (Backend)
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Format code
black backend/

# Lint
flake8 backend/

# Type checking
mypy backend/
```

### JavaScript (Frontend)
```bash
# Install dev dependencies
npm install --save-dev

# Format code
npm run format

# Lint
npm run lint

# Type check
npm run type-check
```

## Adding New Try-On Modules

Create a new module following this pattern:

```
backend/modules/new_category/
├── __init__.py
├── processor.py          # Main processing logic
├── presets/
│   ├── preset-1.json
│   ├── preset-2.json
│   └── schema.json       # Preset validation schema
├── utils.py              # Helper functions
└── tests/
    ├── test_processor.py
    └── test_presets.py
```

### Module Interface
```python
from modules.base import TrialModuleBase

class NewCategoryModule(TrialModuleBase):
    category = "new_category"
    
    def _apply_transformation(self, image, preset):
        # Your implementation here
        pass
    
    def validate_preset(self, preset_id):
        # Validate preset exists and is valid
        pass
```

## Testing

### Required Coverage
- Minimum 80% code coverage
- All public APIs must have tests
- Integration tests for module interactions

```bash
# Run all tests
npm run test
python -m pytest

# With coverage
npm run test:coverage
pytest --cov=backend
```

## Commit Messages

Use conventional commits:
```
feat: add new hair module
fix: resolve image processing bug
docs: update API documentation
test: add processor unit tests
refactor: simplify preset validation
```

## Reporting Bugs

Create an issue with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots/logs if applicable
- Environment (OS, Node/Python version, etc.)

## Suggesting Features

Open a discussion with:
- Use case description
- Proposed solution (if any)
- Alternative solutions
- Implementation complexity estimate

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Recognition

All contributors will be recognized in CONTRIBUTORS.md. Significant architectural contributions may qualify for revenue sharing - discuss with maintainers.

---

**Questions?** Open an issue or contact the maintainers.