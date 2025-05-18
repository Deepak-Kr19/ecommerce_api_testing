# 🛒 E-commerce API Testing Suite

This project is an **automated testing suite** for a mock e-commerce REST API, built using **Python**, **PyTest**, and **Requests**.

## 🔧 Tech Stack

- **Python 3.12**
- **PyTest** – for writing and executing test cases
- **Requests** – for sending HTTP requests to the API

## 📁 Project Structure

ecommerce_api_testing/
│
├── test_api_suite.py # Contains all API test cases
├── requirements.txt # (optional) Package dependencies
└── README.md # Project documentation


## ✅ Features Tested

- **GET** all products
- **GET** single product by ID
- **Edge Case**: Get product with invalid ID
- **POST** login with valid credentials
- **POST** login with invalid password

## 🚀 How to Run

### 1. Clone or Download the Project

```bash
git clone https://github.com/deepak-kr19/ecommerce_api_testing.git
cd ecommerce_api_testing



2. Install Dependencies
        pip install --user pytest requests
    Optionally, create a requirements.txt:
        pip freeze > requirements.txt


3. Run the Tests
    python -m pytest -v
```

    
📌 Sample Output
test_api_suite.py::test_get_all_products PASSED
test_api_suite.py::test_get_single_product PASSED
test_api_suite.py::test_get_invalid_product PASSED
test_api_suite.py::test_user_login_success PASSED
test_api_suite.py::test_user_login_invalid_password PASSED

📚 Learning Objectives
Understand REST API testing concepts

Automate common test cases (CRUD, login)

Handle edge cases and JSON parsing errors

Gain hands-on experience with PyTest

🤝 Contributing
Feel free to fork this repo and add new test cases, such as:

Product creation

Product update

Delete product

Token authorization handling
