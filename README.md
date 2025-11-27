# 📘 Blog API — Open Source REST API

Blog API is an open-source multi-user blogging platform built using Django REST Framework.  
It provides all essential features for a modern blog system:

- JWT Authentication  
- Post CRUD  
- Comment system  
- Like/Unlike functionality  
- Search, filtering, ordering  
- Pagination  
- Rate limiting (throttling)  
- Swagger & Redoc API documentation  

This project is perfect for backend learners and developers building real-world REST APIs.

---

# 🚀 Technologies

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework**
- **SimpleJWT**
- **DRF Spectacular (Swagger / Redoc docs)**
- **Django Filter**

---

# 📦 Installation

```bash
git clone https://github.com/gaybullayevumid/multi-user-blog-api.git
cd blog-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# Authentication (JWT)

All protected endpoints require JWT access tokens.


## Register

```swift
POST /api/users/register/
```

Response
```json
{
  "username": "john",
  "password": "12345"
}
```

## Login

```swift
POST /api/users/login/
```

Response

```json
{
  "access": "jwt-access-token",
  "refresh": "jwt-refresh-token"
}
```

## Authorization header

```makefile
Authorization: Bearer <access_token>
```


# User API

## Get profile

```swift
GET /api/users/profile/
```

## Update profile

```swift
PATCH /api/users/profile/
```


# Posts API

## List posts (with pagination)

```swift
GET /api/posts/
```

## Create post

```swift
POST /api/posts/
```

Response

```json
{
  "content": "My first post!"
}
```

## Get single post

```swift
GET /api/posts/<id>/
```

## Update / Delete

```swift
PATCH /api/posts/<id>/
DELETE /api/posts/<id>/
```

# Comments API

## List comments for a post

```swift
GET /api/posts/<post_id>/comments/
```

## Create comment

```swift
POST /api/posts/<post_id>/comments/
```

Response

```json
{
  "content": "Nice post!"
}
```

# Likes API

## Like / Unlike post

```swift
POST /api/posts/<id>/like/
```

Response

```json
{
  "liked": true,
  "likes_count": 5
}
```

# Search / Filtering / Ordering

## Search

```swift
GET /api/posts/?search=django
```

## Filter by author

```swift
GET /api/posts/?author__username=john
```

## Ordering

```swift
GET /api/posts/?ordering=-created_at
```

# Pagination
Pagination is enabled by default:

```swift
GET /api/posts/?page=2
```
Default page size: 10


# Rate Limiting (Throttling)

```swift
user: 100/minute  
anon: 20/minute  
post_create: 10/minute  
comment_create: 30/minute
```

If the limit is exceeded:

```swift
HTTP 429 Too Many Requests
```

# API Documentation

Swagger UI:

```swift
/api/docs/swagger/
```