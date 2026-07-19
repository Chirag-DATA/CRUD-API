# 🚀 FastAPI CRUD API with PostgreSQL

A simple RESTful API built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL** to perform CRUD (Create, Read, Update, Delete) operations on products. This project is intended for learning FastAPI fundamentals, database integration, and ORM concepts.

---

## 📌 Features

- RESTful API using FastAPI
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request validation
- CRUD operations on products
- Interactive API documentation with Swagger UI
- Automatic table creation using SQLAlchemy

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Language:** Python 3.x
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn
- **Environment Variables:** python-dotenv

---

## 📂 Project Structure

```
fastapi_project/
├──frontend                 # frontend
├── main.py                 # FastAPI application
├── database.py             # Database configuration
├── database_models.py      # SQLAlchemy models
├── models.py               # Pydantic schemas
├── .env                    # Environment variables
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-crud-api.git
cd fastapi-crud-api
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

### 3. Activate the virtual environment

**Windows**

```bash
myenv\Scripts\activate
```

**Linux/macOS**

```bash
source myenv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configure PostgreSQL

Create a `.env` file in the project root.

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
```

---

## ▶️ Run the application

```bash
uvicorn main:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/products` | Get all products |
| GET | `/products/{id}` | Get product by ID |
| POST | `/products` | Create a new product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

---

## 📝 Product Schema

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "Gaming Laptop",
  "price": 65000,
  "quantity": 10
}
```

---

## 🧪 Example Request

### POST `/products`

```json
{
  "id": 5,
  "name": "Keyboard",
  "description": "Mechanical Keyboard",
  "price": 2499,
  "quantity": 8
}
```

---

## 📦 Dependencies

- fastapi
- uvicorn
- sqlalchemy
- psycopg2-binary (or psycopg)
- python-dotenv
- pydantic

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Building REST APIs with FastAPI
- Using SQLAlchemy ORM
- Connecting FastAPI with PostgreSQL
- Environment variable management
- CRUD operations
- Request validation using Pydantic
- Interactive API documentation

---


## 👨‍💻 Author

**Chirag Mittal**

- GitHub: https://github.com/Chirag-DATA
- LinkedIn: https://www.linkedin.com/in/mittal-chirag

---
