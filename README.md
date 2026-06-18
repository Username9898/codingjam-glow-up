# 🎨 Universal Try-On Platform (UTP)

> AI-powered visual transformation engine for hairstyles, outfits, accessories & more.

**Status**: 🚀 In Development | **Version**: 2.0 | **License**: MIT

---

## ⚡ Quick Start

### Prerequisites
```bash
Node.js 18+
Python 3.9+
Docker (optional)
```

### Installation
```bash
# Clone repository
git clone https://github.com/Username9898/codingjam-glow-up.git
cd codingjam-glow-up

# Install dependencies
npm install          # Frontend
pip install -r requirements.txt  # Backend

# Setup environment
cp .env.example .env
```

### Run Locally
```bash
# Development mode
npm run dev          # Frontend on :3000
python -m uvicorn api.main:app --reload  # Backend on :8000
```

---

## 🎯 Features

### Phase 1: MVP (Current)
- ✅ **Hair Try-On**: 4 preset hairstyles
- ✅ **Image Upload**: Drag-and-drop interface
- ✅ **Before/After**: Side-by-side comparison
- ✅ **Vibe Rating**: AI-generated style notes

### Phase 2: Expansion (Q3 2026)
- 🎯 **Outfit Module**: Virtual clothing try-on
- 🎯 **Accessory Module**: Sunglasses, hats, jewelry
- 🎯 **Custom Presets**: User-created styles
- 🎯 **History/Favorites**: Save transformations

### Phase 3: Advanced (Q4 2026)
- 🔮 **Real-time Video**: Live camera preview
- 🔮 **AR Mirror**: Augmented reality mode
- 🔮 **Social Sharing**: Lookbook creation
- 🔮 **Analytics**: Popular styles dashboard

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│   Frontend (React + Tailwind)       │
├─────────────────────────────────────┤
│   API Layer (Node.js/FastAPI)       │
├─────────────────────────────────────┤
│   AI Modules (Pluggable)            │
│   • Hair (HuggingFace)              │
│   • Outfit (Stable Diffusion)       │
│   • Accessories (YOLO/MediaPipe)    │
├─────────────────────────────────────┤
│   Storage (S3 + PostgreSQL)         │
└─────────────────────────────────────┘
```

**Full Details**: See [UNIVERSAL-ARCHITECTURE.md](./UNIVERSAL-ARCHITECTURE.md)

---

## 📁 Project Structure

```
.
├── frontend/                 # React app
│   ├── src/
│   │   ├── components/      # Reusable UI
│   │   ├── modules/         # Try-on modules
│   │   └── App.jsx
│   └── package.json
│
├── backend/                 # API server
│   ├── api/                # Routes & middleware
│   ├── modules/            # Processing logic
│   │   ├── hair/
│   │   ├── outfit/
│   │   └── accessories/
│   ├── utils/              # Helpers
│   └── requirements.txt
│
├── docs/                   # Documentation
│   ├── API.md
│   ├── CONTRIBUTING.md
│   └── DEPLOYMENT.md
│
├── tests/                  # Test suite
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
└── UNIVERSAL-ARCHITECTURE.md
```

---

## 🚀 Deployment

### Docker
```bash
docker-compose up --build
```

### Production (Vercel + Railway)
```bash
# Frontend
vercel deploy --prod

# Backend
railway up --prod
```

See [DEPLOYMENT.md](./docs/DEPLOYMENT.md) for detailed guide.

---

## 🔌 API Endpoints

### Hair Try-On
```bash
POST /api/v1/hair/transform
Content-Type: multipart/form-data

{
  "image": <file>,
  "preset_id": "classic-bangs"
}

Response:
{
  "before": "s3://...",
  "after": "s3://...",
  "vibe_note": "Sophisticated & playful ✨",
  "processing_time_ms": 2341
}
```

### Outfit Try-On
```bash
POST /api/v1/outfit/transform
{
  "image": <file>,
  "preset_id": "casual-summer"
}
```

Full API docs: [API.md](./docs/API.md)

---

## 🧪 Testing

```bash
# Unit tests
npm run test:unit

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Coverage report
npm run test:coverage
```

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

---

## 👥 Contributors

### Founding Contributor
**Roberto Ribeiro** - Platform Architecture & Design  
- 📱 WhatsApp: +55 469 9973-2012
- 🏦 PIX: [Registered]
- Recognition: 1-5% Lifetime Royalty

See [CONTRIBUTORS.md](./CONTRIBUTORS.md) for full credits.

---

## 📊 Tech Stack

| Component | Technology |
|-----------|-------------|
| Frontend | React 18, TypeScript, Tailwind CSS |
| Backend | Node.js/FastAPI, Express/Uvicorn |
| AI/ML | HuggingFace, OpenAI, Stable Diffusion |
| Storage | AWS S3, PostgreSQL, Redis |
| DevOps | Docker, GitHub Actions, Vercel/Railway |

---

## 📈 Roadmap

```
Q2 2026  │  MVP Launch (Hair Module)
         │
Q3 2026  │  Outfit Module
         │  Custom Presets
         │  User History
         │
Q4 2026  │  AR/Video Support
         │  Social Sharing
         │  Analytics Dashboard
         │
2027     │  Mobile App (React Native)
         │  Enterprise Features
```

---

## 💡 Key Innovations

✨ **Modular Architecture** - Add new try-on categories without touching core code  
⚡ **Real-time Processing** - Sub-3s transformation times  
🔒 **Privacy-First** - Images auto-deleted after 24 hours  
📱 **Mobile-Responsive** - Works on all devices  
🌍 **Multi-Language** - i18n support (coming Phase 2)

---

## 📝 License

MIT License - See [LICENSE](./LICENSE)

---

## 🆘 Support

- 📚 **Documentation**: [docs/](./docs/)
- 💬 **Issues**: [GitHub Issues](https://github.com/Username9898/codingjam-glow-up/issues)
- 📧 **Email**: [contact needed]

---

## 🌟 Show Your Support

If you find this project useful:
- ⭐ Star this repository
- 🍴 Fork it and build something amazing
- 📢 Share with your network

---

**Made with ❤️ by the Universal Try-On Team**

*Last Updated: June 18, 2026*