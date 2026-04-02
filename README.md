# Python CRUD API using Requests

This project demonstrates how to perform CRUD operations (Create, Read, Update, Delete) using Python and REST APIs.

The project interacts with a public API (JSONPlaceholder) and performs:

- GET request → retrieve data
- POST request → create data
- PUT request → update data
- DELETE request → delete data

The project is structured into multiple modules for better code organization.

---

## 🚀 Features

- GET API request
- POST API request
- PUT API request
- DELETE API request
- Config file for API settings
- Modular code structure
- Clean and simple implementation
- Beginner-friendly REST API example

---

## 🛠 Tech Stack

- Python 3
- requests library
- REST API
- JSON

Tools:
- VS Code / PyCharm
- Git
- GitHub

API Used:
https://jsonplaceholder.typicode.com

---

## 📂 Project Structure
python-crud-api/
│
├── main.py
├── config.py
├── get_request.py
├── post_request.py
├── put_request.py
├── delete_request.py
└── README.md

---

## ⚙️ Configuration

config.py file contains API configuration:
BASE_URL = "http://jsonplaceholder.typicode.com"
HEADERS = {
"Content-Type": "application/json"
}

---

## 🌐 API Used

Public test API:

https://jsonplaceholder.typicode.com

Example endpoint:
GET /posts
POST /posts
PUT /posts/1
DELETE /posts/1


---

## 🎯 Learning Objectives

This project helps understand:

- REST API fundamentals
- HTTP methods (GET, POST, PUT, DELETE)
- Working with external APIs
- Python modular coding
- Using config file for settings
- JSON request & response handling

---

## 🔮 Future Improvements

- Add error handling
- Add logging
- Add environment variables (.env)
- Convert to FastAPI project
- Add unit tests

---

## 👨‍💻 Author
MD Sahil Siddiquie

Python Backend Developer

GitHub:
https://github.com/siddiquie696-cloud

---

## ⭐ Support

If this project helps you learn, give it a star on GitHub.
