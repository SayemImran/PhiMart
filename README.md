# 🛒 PhiMart – E-commerce REST API

PhiMart is a fully-featured e-commerce backend built with **Django Rest Framework (DRF)**.  
It provides RESTful APIs for managing products, categories, carts, and orders, with secure **JWT authentication** and interactive **Swagger API documentation**.

---

## 🚀 Features

- User authentication & authorization using **JWT (Djoser)**
- Product & category management
- Shopping cart functionality
- Order creation & management
- Secure API endpoints
- Auto-generated API documentation (Swagger / Redoc)
- Clean, scalable REST architecture

---

## 🛠️ Tech Stack

- **Python**
- **Django**
- **Django Rest Framework**
- **Djoser** (JWT Authentication)
- **drf-yasg** (Swagger Documentation)
- **SQLite / PostgreSQL** (configurable)
- **JWT (JSON Web Tokens)**

---

## 📂 Project Structure
```text
PhiMart/
│
├── products/
├── categories/
├── carts/
├── orders/
├── users/
├── config/
├── manage.py
└── requirements.txt
```


---

## 🔐 Authentication

Authentication is handled using **Djoser with JWT**.

### Available Auth Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/auth/jwt/create/` | Login |
| POST | `/auth/jwt/refresh/` | Refresh token |
| POST | `/auth/users/` | Register user |
| GET  | `/auth/users/{user_id}/` | Get current user |
| GET  | `/api/products/` | Get all products |
| GET  | `/api/categories/` | Get all categories |
| GET  | `/api/orders/` | Get all Orders |
| GET  | `/api/orders/{user_id}` | Get Order of user |
| GET  | `/api/carts/` | Get all Carts |
| GET  | `/api/carts/{user_id}` | Get Cart of user |

---
## 📘 API Documentation

Swagger documentation is available at:

- **Swagger UI:**
```bash
http://127.0.0.1:8000/swagger/
```

- **ReDoc:**  
```bash
http://127.0.0.1:8000/redoc/
```
---

## 📦 API Modules

### Products
- List products
- Retrieve product details
- Create / update / delete products (admin only)

### Categories
- List categories
- Retrieve category details

### Cart
- Add items to cart
- Update cart items
- Remove items
- View cart

### Orders
- Place orders
- View order history
- Order details

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/phimart.git
cd phimart
```
### 2️⃣ Create the virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Run migrations
```bash
python manage.py migrate
```
### 6️⃣ Create superuser
```bash
python manage.py createsuperuser
```
### 7️⃣ Run the server
```bash
python manage.py runserver
```
