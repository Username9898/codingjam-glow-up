# Contributing to Universal Try-On Platform

We're excited to have you contribute! Whether it's code, documentation, bug reports, or feature suggestions — all contributions are valued.

This guide will help you get started smoothly.

---

## 🚀 Quick Start for Contributors

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/your-username/codingjam-glow-up.git`
3. **Create** a branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes
5. **Test** thoroughly
6. **Push** and open a Pull Request

---

## 📋 Development Setup

### Prerequisites
```bash
Node.js 18+
Python 3.9+
Git
```

### Install Development Tools

#### Frontend
```bash
cd frontend
npm install
npm install --save-dev  # Dev dependencies
```

#### Backend
```bash
cd backend
pip install -r requirements-dev.txt
```

---

## 💻 Development Workflow

### Create Feature Branch
```bash
# Use conventional naming
git checkout -b feature/hair-module-improvements
git checkout -b fix/image-upload-bug
git checkout -b docs/api-examples
```

### Code Quality Standards

#### Python (Backend)

**Install Tools**
```bash
pip install black flake8 mypy pytest pytest-cov
```

**Format Code**
```bash
black backend/
```

**Lint**
```bash
flake8 backend/ --max-line-length=100
```

**Type Check**
```bash
mypy backend/ --ignore-missing-imports
```

**Run Tests**
```bash
pytest backend/tests/ --cov=backend --cov-report=html
```

#### JavaScript (Frontend)

**Install Tools**
```bash
npm install --save-dev eslint prettier typescript
```

**Format Code**
```bash
npm run format
# Or manually: npx prettier --write src/
```

**Lint**
```bash
npm run lint
```

**Type Check**
```bash
npm run type-check
# Runs tsc --noEmit
```

**Run Tests**
```bash
npm run test:unit
npm run test:coverage
```

### Before Committing

```bash
# 1. Format code
npm run format          # Frontend
black backend/          # Backend

# 2. Lint
npm run lint            # Frontend
flake8 backend/         # Backend

# 3. Type check
npm run type-check      # Frontend
mypy backend/           # Backend

# 4. Run tests
npm run test:coverage   # Frontend
pytest --cov backend/   # Backend

# 5. Check coverage (minimum 80%)
npm run test:coverage   # Generates report
```

---

## 📝 Commit Messages

Use **Conventional Commits** format:

```
type(scope): subject

body (optional)

footer (optional)
```

### Types
- `feat` — New feature
- `fix` — Bug fix
- `docs` — Documentation changes
- `style` — Formatting (no code logic changes)
- `refactor` — Code restructuring
- `perf` — Performance improvements
- `test` — Test additions/changes
- `chore` — Build, CI, dependency updates
- `ci` — CI/CD pipeline changes

### Examples
```bash
git commit -m "feat(hair): add new curly texture preset"
git commit -m "fix(upload): resolve image orientation issue"
git commit -m "docs(api): add authentication examples"
git commit -m "test(outfit): increase module coverage to 85%"
git commit -m "refactor(utils): simplify image processing pipeline"
```

---

## 🧩 Adding New Try-On Modules

### Module Structure

```
backend/modules/new_category/
├── __init__.py
├── processor.py          # Core transformation logic
├── presets/
│   ├── preset-1.json     # Preset configuration
│   ├── preset-2.json
│   └── schema.json       # JSON schema for validation
├── utils.py              # Helper functions
├── tests/
│   ├── __init__.py
│   ├── test_processor.py
│   ├── test_presets.py
│   └── fixtures/
│       ├── sample_image.jpg
│       └── expected_output.jpg
└── README.md             # Module documentation
```

### Base Module Interface

```python
from modules.base import TrialModuleBase
from typing import Dict, Optional
import numpy as np

class NewCategoryModule(TrialModuleBase):
    """Try-on module for new_category transformations."""
    
    category = "new_category"
    version = "1.0.0"
    max_processing_time_ms = 3000
    
    def __init__(self):
        super().__init__()
        self.model = self._load_model()
    
    def _apply_transformation(self, image: np.ndarray, preset: Dict) -> np.ndarray:
        """
        Apply transformation to image.
        
        Args:
            image: Input image as numpy array (H, W, 3)
            preset: Preset configuration dictionary
            
        Returns:
            Transformed image as numpy array
            
        Raises:
            ValueError: If preset is invalid
            RuntimeError: If transformation fails
        """
        # Your implementation here
        pass
    
    def validate_preset(self, preset_id: str) -> bool:
        """Validate that preset exists and is valid."""
        # Check preset exists in presets/
        # Validate against schema.json
        pass
    
    def get_presets(self) -> Dict:
        """Return all available presets for this module."""
        pass
    
    def _load_model(self):
        """Load AI model (HuggingFace, ONNX, etc.)."""
        pass
```

### Example Preset Configuration

```json
{
  "id": "preset-1",
  "name": "Stylish Look",
  "description": "Modern and trendy style",
  "category": "new_category",
  "difficulty": "easy",
  "parameters": {
    "intensity": 0.8,
    "color_adjustment": true,
    "edge_smoothing": 2.0
  },
  "preview_url": "s3://bucket/preset-preview-1.jpg",
  "compatible_attributes": ["skin_tone", "face_shape"],
  "version": "1.0.0"
}
```

### Testing Your Module

```python
# backend/modules/new_category/tests/test_processor.py

import pytest
import numpy as np
from PIL import Image
from modules.new_category import NewCategoryModule

@pytest.fixture
def module():
    return NewCategoryModule()

@pytest.fixture
def sample_image():
    # Create or load test image
    img = Image.new('RGB', (640, 480), color='red')
    return np.array(img)

def test_transformation_basic(module, sample_image):
    """Test basic transformation."""
    preset = module.get_presets()['presets'][0]
    result = module.transform(sample_image, preset)
    
    assert result.shape == sample_image.shape
    assert result.dtype == np.uint8

def test_preset_validation(module):
    """Test preset validation."""
    assert module.validate_preset("preset-1") == True
    assert module.validate_preset("invalid-id") == False

def test_processing_performance(module, sample_image):
    """Test processing stays under time limit."""
    import time
    preset = module.get_presets()['presets'][0]
    
    start = time.time()
    module.transform(sample_image, preset)
    elapsed = (time.time() - start) * 1000
    
    assert elapsed < module.max_processing_time_ms
```

---

## 🔄 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines (run formatters & linters)
- [ ] New features have tests (minimum 80% coverage)
- [ ] Documentation is updated
- [ ] Commit messages follow Conventional Commits
- [ ] No merge conflicts with main branch
- [ ] Tested locally

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Related Issues
Closes #123

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## How Has This Been Tested?
Describe the testing you did.

## Screenshots (if applicable)
Add before/after screenshots or demos.

## Checklist
- [ ] My code follows style guidelines
- [ ] I have performed a self-review
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass locally
```

### Review Process

1. Automated checks must pass (linting, tests, coverage)
2. Code review from maintainers
3. All conversations resolved
4. Approval required before merge
5. Squash commits on merge

---

## 🐛 Reporting Bugs

### Create an Issue With

- **Clear title**: "Fix specific problem in module X"
- **Description**: What happened vs. expected behavior
- **Steps to reproduce**: Exact sequence to trigger bug
- **Environment**: OS, Node/Python version, etc.
- **Screenshots/logs**: Visual evidence if applicable
- **Code snippet**: Minimal reproducible example

### Example Bug Report

```markdown
## Bug: Hair preset crashes on large images

### Description
The classic-bangs preset crashes when processing images larger than 2000x2000 pixels.

### Steps to Reproduce
1. Upload a 3000x3000 image
2. Select "classic-bangs" preset
3. Click "Transform"
4. Error occurs

### Expected Behavior
Image should resize automatically and transform successfully.

### Actual Behavior
Backend returns 500 error: "CUDA out of memory"

### Environment
- OS: Ubuntu 20.04
- Python: 3.9.10
- GPU: NVIDIA RTX 3080

### Error Log
```
RuntimeError: CUDA out of memory. Tried to allocate 2.50 GiB...
  File "processor.py", line 156, in _apply_transformation
```
```

---

## 💡 Suggesting Features

### Create a Discussion With

- **Use case**: Why would users need this?
- **Proposed solution**: Your idea (optional)
- **Alternative approaches**: Other ways to solve it
- **Implementation complexity**: Easy / Medium / Hard
- **Impact**: How many users would benefit?

### Example Feature Request

```markdown
## Feature: Real-time video preview

### Use Case
Users want to see how hairstyles look before uploading a photo. Real-time video preview using webcam would let them experiment without uploading.

### Proposed Solution
Add a video mode that:
1. Accesses user's webcam (with permission)
2. Runs hair transformation 24fps
3. Shows before/after side-by-side
4. Includes "Capture" button to save frames

### Alternative Approaches
- Desktop app with better GPU support
- Browser-based with Web Workers for background processing

### Implementation Complexity
Hard (requires WebRTC, real-time ML inference)

### Impact
Would benefit ~60% of mobile users based on competitor analysis
```

---

## 📚 Documentation

### When Adding Features, Update:

- [ ] **README.md** — Add feature description & usage
- [ ] **API.md** — Document new endpoints
- [ ] **ARCHITECTURE.md** — Update system diagrams if needed
- [ ] **Code comments** — Explain complex logic
- [ ] **Module README** — Document new module if applicable

### Documentation Standards

```python
def transform(self, image: np.ndarray, preset: Dict) -> np.ndarray:
    """
    Apply transformation to image using specified preset.
    
    This is the main entry point for all transformations. It handles:
    - Input validation
    - Model inference
    - Output post-processing
    
    Args:
        image: Input image as numpy array with shape (height, width, 3).
               Must be RGB format with values in [0, 255].
        preset: Configuration dict with keys:
            - 'id' (str): Preset identifier
            - 'intensity' (float, 0-1): Strength of effect
            - 'options' (dict): Preset-specific parameters
    
    Returns:
        Transformed image as numpy array with same shape and dtype as input.
    
    Raises:
        ValueError: If preset_id not found or image format invalid.
        RuntimeError: If transformation fails (e.g., GPU error).
    
    Examples:
        >>> image = cv2.imread('photo.jpg')
        >>> preset = {'id': 'classic', 'intensity': 0.8}
        >>> result = module.transform(image, preset)
        >>> cv2.imwrite('result.jpg', result)
    
    Notes:
        - Processing time: ~2-3 seconds on GPU
        - Image is auto-resized to 640x480 if needed
        - Output format matches input format
    """
```

---

## 🎯 Code Review Checklist

When reviewing PRs, check:

- **Functionality**: Does it work as intended?
- **Tests**: Are there tests? Do they pass?
- **Coverage**: Does it maintain 80%+ coverage?
- **Performance**: Any major performance issues?
- **Security**: Any security concerns?
- **Documentation**: Is it documented?
- **Style**: Does it follow guidelines?
- **Readability**: Is code understandable?

---

## 🏆 Recognition

All contributors are recognized in [CONTRIBUTORS.md](./CONTRIBUTORS.md).

- **Bug fixes**: Credit in PR
- **Features**: Named contributor for the feature
- **Major contributions**: May qualify for revenue sharing (discuss with maintainers)

---

## 📞 Need Help?

- 📖 Read the [README.md](./README.md)
- 📚 Check [docs/](./docs/) folder
- 🐛 Search existing [issues](https://github.com/Username9898/codingjam-glow-up/issues)
- 💬 Join [discussions](https://github.com/Username9898/codingjam-glow-up/discussions)
- 📧 Contact maintainers

---

## 📄 License

By contributing, you agree your contributions will be licensed under the MIT License.

---

<div align="center">

**Thank you for contributing to Universal Try-On! 🎉**

[🔝 Back to top](#contributing-to-universal-try-on-platform)

</div>
