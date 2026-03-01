# 📝 Smart ToDo API

A RESTful backend application for task management built using **FastAPI** and **MongoDB**, featuring **JWT-based user authentication** and full **CRUD operations** for tasks.

This project was developed as part of an **Intern Technical Assessment**.

---

## 🚀 Features

- User Registration & Login (JWT Authentication)
- Secure password hashing (bcrypt)
- Create, Read, Update, Delete (CRUD) tasks
- Each user can access only their own tasks
- MongoDB (NoSQL) database integration
- Automatic API documentation using Swagger UI

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** MongoDB (NoSQL)
- **Authentication:** JWT (JSON Web Tokens)
- **Password Hashing:** passlib + bcrypt
- **API Documentation:** Swagger UI
- **Server:** Uvicorn

---

## 📁 Project Structure

```text
smart-todo-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── auth.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── auth_routes.py
│       └── task_routes.py
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Prerequisites

- Python **3.11.x**
- MongoDB Community Edition
- Git

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/Barun-007/Intern-Technical-Assessment/tree/main/smart-todo-api
cd smart-todo-api
```

### 3️⃣ Create and Activate Virtual Environment
```bash
python -m venv myenv
myenv\Scripts\activate
```
### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Start MongoDB
Ensure MongoDB service is running on your system.

(Optional check)
```bash
mongod --version
```

### 6️⃣ Run the Application
```bash
uvicorn app.main:app --reload
```
Server will start at:
```cpp
http://127.0.0.1:8000
```
### 📄 API Documentation (Swagger)

FastAPI automatically generates interactive API documentation.

🔗 Swagger UI URL:

http://localhost:8000/docs


> Note: This project runs locally. After starting the server, open the above link to view and test all APIs.