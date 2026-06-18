# Universal Try-On Platform - API Documentation

## Base URL
```
Development: http://localhost:8000
Production: https://api.universal-tryon.app
```

## Authentication
All endpoints require a valid API key in the header:
```
Authorization: Bearer YOUR_API_KEY
```

---

## Hair Try-On Endpoints

### Transform Image
**POST** `/api/v1/hair/transform`

Transform a selfie with a selected hairstyle preset.

**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/hair/transform \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "image=@photo.jpg" \
  -F "preset_id=classic-bangs"
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| image | file | ✓ | JPG/PNG selfie (max 10MB) |
| preset_id | string | ✓ | Preset ID (see below) |
| return_metadata | boolean | | Include processing details |

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "before": "https://s3.amazonaws.com/.../before.jpg",
    "after": "https://s3.amazonaws.com/.../after.jpg",
    "vibe_note": "Sophisticated & playful ✨",
    "metadata": {
      "preset_id": "classic-bangs",
      "preset_name": "Classic Bangs",
      "processing_time_ms": 2341,
      "confidence": 0.94,
      "face_detected": true
    }
  }
}
```

**Error Responses:**
```json
{
  "success": false,
  "error": {
    "code": "NO_FACE_DETECTED",
    "message": "Could not detect a face in the image. Please try a clear selfie.",
    "status": 422
  }
}
```

---

### List Presets
**GET** `/api/v1/hair/presets`

Get all available hairstyle presets.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": "classic-bangs",
      "name": "Classic Bangs",
      "description": "Shoulder-length with face-framing bangs",
      "category": "hair",
      "thumbnail": "https://s3.amazonaws.com/.../classic-bangs.jpg",
      "vibe_notes": "Sophisticated & playful ✨",
      "tags": ["feminine", "timeless", "face-framing"]
    },
    {
      "id": "long-waves",
      "name": "Long Waves",
      "description": "Long, voluminous waves for a glamorous look",
      "category": "hair",
      "thumbnail": "https://s3.amazonaws.com/.../long-waves.jpg",
      "vibe_notes": "Glamorous & confident 💫",
      "tags": ["long", "waves", "glamorous"]
    }
  ],
  "total": 4
}
```

---

### Get Preset Details
**GET** `/api/v1/hair/presets/{preset_id}`

Get detailed information about a specific preset.

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": "classic-bangs",
    "name": "Classic Bangs",
    "description": "Shoulder-length with face-framing bangs",
    "model_version": "2024-q1",
    "api_provider": "huggingface",
    "parameters": {
      "style_vector": [0.12, -0.45, 0.88, ...],
      "strength": 0.85,
      "preserve_skin_tone": true
    },
    "vibe_notes": "Sophisticated & playful ✨",
    "thumbnail": "https://s3.amazonaws.com/.../classic-bangs.jpg",
    "examples": [
      "https://s3.amazonaws.com/.../example1.jpg",
      "https://s3.amazonaws.com/.../example2.jpg"
    ]
  }
}
```

---

## Outfit Try-On Endpoints

### Transform Image
**POST** `/api/v1/outfit/transform`

Transform a full-body photo with a selected outfit preset.

**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/outfit/transform \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "image=@fullbody.jpg" \
  -F "preset_id=casual-summer"
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| image | file | ✓ | JPG/PNG photo (max 10MB) |
| preset_id | string | ✓ | Outfit preset ID |

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "before": "https://s3.amazonaws.com/.../before.jpg",
    "after": "https://s3.amazonaws.com/.../after.jpg",
    "outfit_details": {
      "top": "White Linen Shirt",
      "bottom": "Denim Shorts",
      "accessories": "Straw Hat",
      "colors": ["#FFFFFF", "#4A90E2", "#D4A574"]
    },
    "metadata": {
      "preset_id": "casual-summer",
      "processing_time_ms": 3421,
      "confidence": 0.88
    }
  }
}
```

---

### List Outfit Presets
**GET** `/api/v1/outfit/presets`

Get all available outfit presets.

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": "casual-summer",
      "name": "Casual Summer",
      "description": "Light, breathable summer outfit",
      "thumbnail": "https://s3.amazonaws.com/.../casual-summer.jpg",
      "mood": "Relaxed & Breezy 🌞"
    }
  ],
  "total": 6
}
```

---

## Accessory Try-On Endpoints

### Transform Image
**POST** `/api/v1/accessories/transform`

Add accessories to a photo (sunglasses, hats, jewelry).

**Request:**
```bash
curl -X POST http://localhost:8000/api/v1/accessories/transform \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -F "image=@photo.jpg" \
  -F "accessory_type=sunglasses" \
  -F "preset_id=aviator-gold"
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| image | file | ✓ | JPG/PNG photo (max 10MB) |
| accessory_type | string | ✓ | Type: sunglasses, hats, jewelry, watches |
| preset_id | string | ✓ | Specific accessory preset ID |

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "before": "https://s3.amazonaws.com/.../before.jpg",
    "after": "https://s3.amazonaws.com/.../after.jpg",
    "accessory_details": {
      "type": "sunglasses",
      "style": "Aviator",
      "material": "Gold-plated",
      "brand": "Designer"
    }
  }
}
```

---

## User History Endpoints

### Get User Transformations
**GET** `/api/v1/user/history`

Retrieve all transformations created by the user.

**Query Parameters:**
| Name | Type | Default | Description |
|------|------|---------|-------------|
| limit | integer | 20 | Results per page (max 100) |
| offset | integer | 0 | Pagination offset |
| category | string | | Filter by category (hair, outfit, accessories) |
| date_from | ISO8601 | | Filter from date |

**Response (200 OK):**
```json
{
  "success": true,
  "data": [
    {
      "id": "txn_abc123",
      "category": "hair",
      "preset_id": "classic-bangs",
      "before_image": "https://...",
      "after_image": "https://...",
      "created_at": "2026-06-18T15:30:00Z",
      "is_favorite": true
    }
  ],
  "pagination": {
    "limit": 20,
    "offset": 0,
    "total": 145
  }
}
```

### Save Favorite
**POST** `/api/v1/user/favorites`

Mark a transformation as favorite.

**Request:**
```json
{
  "transformation_id": "txn_abc123"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "data": {
    "transformation_id": "txn_abc123",
    "is_favorite": true
  }
}
```

---

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| INVALID_IMAGE | 400 | Image format not supported or corrupted |
| NO_FACE_DETECTED | 422 | Could not detect face in image |
| INVALID_PRESET | 400 | Preset ID does not exist |
| RATE_LIMIT_EXCEEDED | 429 | Too many requests (50/min per user) |
| UNAUTHORIZED | 401 | Invalid or missing API key |
| INTERNAL_ERROR | 500 | Server error - retry later |

---

## Rate Limiting

All endpoints are rate-limited:
- **Free tier**: 50 requests/minute
- **Pro tier**: 500 requests/minute
- **Enterprise**: Custom limits

Headers returned:
```
X-RateLimit-Limit: 50
X-RateLimit-Remaining: 48
X-RateLimit-Reset: 1624056000
```

---

## Examples

### Python
```python
import requests

API_KEY = "your_api_key"
headers = {"Authorization": f"Bearer {API_KEY}"}

with open("selfie.jpg", "rb") as f:
    files = {"image": f}
    data = {"preset_id": "classic-bangs"}
    
    response = requests.post(
        "http://localhost:8000/api/v1/hair/transform",
        headers=headers,
        files=files,
        data=data
    )
    
    result = response.json()
    print(f"Before: {result['data']['before']}")
    print(f"After: {result['data']['after']}")
```

### JavaScript
```javascript
const formData = new FormData();
formData.append('image', imageFile);
formData.append('preset_id', 'classic-bangs');

const response = await fetch('/api/v1/hair/transform', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${API_KEY}`
  },
  body: formData
});

const result = await response.json();
```

---

**Last Updated**: June 18, 2026  
**Version**: 1.0
