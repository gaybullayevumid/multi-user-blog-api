# 📘 Multi-User Blog API

Professional multi-user blogging platform REST API built with Django REST Framework.

[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16-red.svg)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)

## ✨ Features

- 🔐 JWT Authentication (Access & Refresh Tokens)
- 👤 User Registration & Profile Management
- 📝 Full CRUD for Blog Posts
- 💬 Comment System
- ❤️ Like/Unlike Posts
- 🔍 Advanced Search & Filtering
- 📄 Pagination
- ⚡ Rate Limiting (Throttling)
- 📚 Interactive API Documentation (Swagger & ReDoc)
- 🚀 Optimized Database Queries
- 🔒 Permission-based Access Control
- 🌐 CORS Support
- 📸 Image Upload Support

## 🛠️ Tech Stack

- **Python 3.13+**
- **Django 5.2**
- **Django REST Framework 3.16**
- **SimpleJWT** - JWT Authentication
- **DRF Spectacular** - API Documentation
- **Django Filter** - Advanced Filtering
- **Django CORS Headers** - CORS Support
- **Pillow** - Image Processing

## 📦 Installation

### 1. Clone Repository

```bash
git clone https://github.com/gaybullayevumid/multi-user-blog-api.git
cd multi-user-blog-api
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create `.env` file (or copy from `.env.example`):

```bash
cp .env.example .env
```

Update `.env` with your settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Server

```bash
python manage.py runserver
```

Server will run at: `http://127.0.0.1:8000/`

## 📖 API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/api/docs/swagger/`
- **ReDoc**: `http://127.0.0.1:8000/api/docs/redoc/`
- **OpenAPI Schema**: `http://127.0.0.1:8000/api/schema/`

## 🔑 Authentication

### Register User

```http
POST /api/signup/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!"
}
```

### Login

```http
POST /api/login/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Refresh Token

```http
POST /api/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Logout

```http
POST /api/logout/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Authorization Header

For protected endpoints, include:

```http
Authorization: Bearer <access_token>
```

## 👤 User Endpoints

### Get Profile

```http
GET /api/profile/
Authorization: Bearer <access_token>
```

### Update Profile

```http
PATCH /api/profile/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
  "bio": "Software Developer",
  "avatar": <file>
}
```

## 📝 Post Endpoints

### List Posts (Paginated)

```http
GET /api/posts/
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `page` - Page number
- `search` - Search in title, content, author
- `author__username` - Filter by author
- `ordering` - Sort by field (created_at, updated_at)

### Create Post

```http
POST /api/posts/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
  "title": "My First Post",
  "content": "Post content here...",
  "image": <file>
}
```

### Get Single Post

```http
GET /api/post/<id>/
Authorization: Bearer <access_token>
```

### Update Post (Author Only)

```http
PATCH /api/post/<id>/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Updated Title",
  "content": "Updated content..."
}
```

### Delete Post (Author Only)

```http
DELETE /api/post/<id>/
Authorization: Bearer <access_token>
```

## 💬 Comment Endpoints

### List Comments for Post

```http
GET /api/posts/<post_id>/comments/
```

**Query Parameters:**
- `search` - Search in content
- `author__username` - Filter by author
- `ordering` - Sort by created_at

### Create Comment

```http
POST /api/posts/<post_id>/comments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "content": "Great post!"
}
```

### Update Comment (Author Only)

```http
PATCH /api/comments/<id>/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "content": "Updated comment"
}
```

### Delete Comment (Author Only)

```http
DELETE /api/comments/<id>/
Authorization: Bearer <access_token>
```

## ❤️ Like Endpoints

### Toggle Like

```http
POST /api/posts/<post_id>/like/
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "message": "Post liked",
  "liked": true
}
```

## 📊 Project Structure

```
multi-user-blog-api/
├── apps/
│   ├── comments/          # Comment app
│   ├── likes/             # Like app
│   ├── posts/             # Post app
│   └── users/             # User app
├── config/                # Django settings
├── media/                 # Uploaded files
├── staticfiles/           # Static files
├── .env.example           # Environment variables template
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Configuration

### Rate Limiting

Default throttle rates (in `settings.py`):

```python
'DEFAULT_THROTTLE_RATES': {
    'user': '1000/hour',
    'anon': '100/hour',
    'post_create': '20/hour',
    'comment_create': '50/hour',
}
```

### Pagination

Default page size: 10 items per page

### CORS

Configure allowed origins in `.env`:

```env
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

## 🔒 Security Features

- Environment-based SECRET_KEY
- Password validation
- JWT token authentication
- Permission-based access control
- Rate limiting
- CORS configuration
- Secure file uploads

## 🧪 Testing

```bash
python manage.py test
```

## 📝 Development

### Format Code

```bash
black .
```

### Create Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Umid Gaybullayev**

- GitHub: [@gaybullayevumid](https://github.com/gaybullayevumid)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!
