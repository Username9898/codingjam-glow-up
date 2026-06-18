# Universal Try-On Platform (UTP) v2.0

## 🎯 Vision

Transformar o AI Hairstyle Try-On em uma **plataforma modular universal** que suporte múltiplas categorias de transformação digital em tempo real.

## 📋 Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│         USER INTERFACE LAYER (React/Vue)                │
├─────────────────────────────────────────────────────────┤
│  • Image Upload Manager                                 │
│  • Category Selector (Hair, Outfit, Accessories, etc.)  │
│  • Preset Gallery                                       │
│  • Real-time Preview Canvas                             │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│     API ORCHESTRATION LAYER (Node.js/Python)            │
├─────────────────────────────────────────────────────────┤
│  • Request Router                                       │
│  • Authentication & Rate Limiting                       │
│  • File Upload Handler                                  │
│  • Response Formatter                                   │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│      AI/ML PROCESSING LAYER (Modular)                   │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Hair Module │  │ Outfit Mod.  │  │Accessory Mod. │  │
│  │  (Hugging   │  │  (Rembg +    │  │  (YOLO +      │  │
│  │   Face)     │  │  Stable)     │  │  Overlay)     │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
│                                                         │
│  All modules: OpenAI API / Replicate / Hugging Face   │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│      DATA & STORAGE LAYER                               │
├─────────────────────────────────────────────────────────┤
│  • S3 / GCS (Image Cache)                              │
│  • PostgreSQL (User History)                           │
│  • Redis (Session Cache)                               │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Module Structure

### 1. **Hair Try-On Module** (Original)
```python
# /modules/hair/
├── presets/
│   ├── classic-bangs.json
│   ├── long-waves.json
│   ├── pixie-cut.json
│   └── undercut.json
├── processor.py
├── style_descriptor.py
└── tests/
```

**Input**: Selfie + preset selection  
**Output**: Before/after comparison + vibe rating  
**API**: Hugging Face (face-detection) + OpenAI DALL-E (style transfer)

### 2. **Outfit Try-On Module** (Expandable)
```python
# /modules/outfit/
├── presets/
│   ├── casual-summer.json
│   ├── formal-evening.json
│   ├── streetwear-vibes.json
│   └── minimalist.json
├── body_segmentation.py
├── cloth_processor.py
└── tests/
```

**Input**: Full-body photo + outfit preset  
**Output**: Virtual try-on with outfit overlay  
**API**: Rembg (background removal) + Stable Diffusion (outfit synthesis)

### 3. **Accessories Module** (Expandable)
```python
# /modules/accessories/
├── presets/
│   ├── sunglasses/
│   ├── hats/
│   ├── jewelry/
│   └── watches/
├── pose_detector.py
├── overlay_engine.py
└── tests/
```

**Input**: Face/body photo + accessory type  
**Output**: Real-time augmented reality overlay  
**API**: MediaPipe (pose detection) + custom overlay algorithms

---

## 🚀 Core Features (Phase 1-3)

### Phase 1: MVP (Weeks 1-2)
- ✅ Hair module (4 presets)
- ✅ Single image upload
- ✅ Vibe rating system
- ✅ Before/after comparison

### Phase 2: Expansion (Weeks 3-4)
- 🎯 Outfit module (basic)
- 🎯 Multi-category support
- 🎯 Preset customization UI
- 🎯 History/favorites

### Phase 3: Advanced (Weeks 5+)
- 🔮 Real-time video preview
- 🔮 AR mirror mode
- 🔮 Social sharing + lookbooks
- 🔮 Custom preset creation
- 🔮 Analytics dashboard

---

## 💻 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 / TypeScript / Tailwind CSS |
| **Backend** | Node.js + Express / Python FastAPI |
| **AI/ML** | Hugging Face / OpenAI / Stable Diffusion |
| **Storage** | AWS S3 / PostgreSQL |
| **Cache** | Redis / Varnish |
| **CI/CD** | GitHub Actions |
| **Hosting** | Vercel (Frontend) / Railway/Render (Backend) |

---

## 📁 Project Structure

```
codingjam-glow-up/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUpload.jsx
│   │   │   ├── PresetGallery.jsx
│   │   │   ├── BeforeAfter.jsx
│   │   │   └── VibeRating.jsx
│   │   ├── modules/
│   │   │   ├── HairTryOn.jsx
│   │   │   ├── OutfitTryOn.jsx
│   │   │   └── AccessoryTryOn.jsx
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── api/
│   │   ├── routes.py
│   │   ├── auth.py
│   │   └── middleware.py
│   ├── modules/
│   │   ├── hair/
│   │   ├── outfit/
│   │   └── accessories/
│   ├── utils/
│   │   ├── image_processor.py
│   │   ├── storage.py
│   │   └── cache.py
│   ├── config.py
│   └── requirements.txt
│
├── docs/
│   ├── API.md
│   ├── CONTRIBUTING.md
│   └── DEPLOYMENT.md
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── UNIVERSAL-ARCHITECTURE.md (this file)
├── README.md
├── docker-compose.yml
└── .github/
    └── workflows/
        ├── test.yml
        ├── deploy.yml
        └── lint.yml
```

---

## 🔑 Key Concepts

### Category Module Pattern
Cada nova categoria segue este padrão:

```python
class TrialModuleBase:
    """Base class for all try-on modules"""
    
    def __init__(self, presets_path: str):
        self.presets = self.load_presets(presets_path)
    
    def process(self, image: PIL.Image, preset_id: str) -> Dict:
        """Process image with selected preset"""
        validated_preset = self.validate_preset(preset_id)
        result = self._apply_transformation(image, validated_preset)
        return self._format_output(result)
    
    def _apply_transformation(self, image, preset):
        """Override in subclass"""
        raise NotImplementedError
    
    def _format_output(self, result) -> Dict:
        """Standardized output format"""
        return {
            "before": result.get("original"),
            "after": result.get("transformed"),
            "metadata": {
                "category": self.category,
                "preset": result.get("preset_name"),
                "processing_time_ms": result.get("duration"),
                "confidence": result.get("confidence")
            }
        }
```

### Preset Schema
```json
{
  "id": "classic-bangs",
  "category": "hair",
  "name": "Classic Bangs",
  "description": "Shoulder-length with face-framing bangs",
  "model_version": "2024-q1",
  "api_provider": "huggingface",
  "parameters": {
    "style_vector": [...],
    "strength": 0.85,
    "preserve_skin_tone": true
  },
  "thumbnail": "s3://bucket/presets/classic-bangs.jpg",
  "vibe_notes": "Sophisticated & playful ✨"
}
```

---

## 🔐 Security & Privacy

- [ ] Images deleted after 24 hours
- [ ] End-to-end encryption for uploads
- [ ] GDPR compliance
- [ ] Rate limiting (50 req/min per user)
- [ ] Input validation & sanitization
- [ ] API key rotation every 30 days

---

## 📊 Metrics & Analytics

Track via:
- **Conversion**: Uploads → Transformations
- **Engagement**: Time in app, repeat users
- **Performance**: API latency, error rates
- **Popular Presets**: Which styles users prefer
- **Hardware**: CPU/GPU utilization

---

## 🤝 Contributing

See `CONTRIBUTING.md` for:
- Code standards
- Pull request process
- Module development guidelines
- Testing requirements

---

## 📝 License

MIT License - See LICENSE file

---

## ✨ Contributors & Credits

**Original Concept**: Coding Jam Week 1  
**Architecture & Expansion**: Universal Try-On Platform Team

---

**Last Updated**: June 2026  
**Version**: 2.0 (Universal)
