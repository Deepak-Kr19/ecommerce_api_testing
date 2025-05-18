import requests

BASE_URL = "https://fakestoreapi.com"

# 1. Get All Products
def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]

# 2. Get Single Product by ID
def test_get_single_product():
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert "title" in product

# 3. Invalid Product ID
def test_get_invalid_product():
    response = requests.get(f"{BASE_URL}/products/9999")
    assert response.status_code in [200, 404]

    if response.status_code == 200:
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            data = None
        assert data == {} or data is None


# 4. Successful Login
def test_user_login_success():
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

# 5. Invalid Login
def test_user_login_invalid_password():
    payload = {
        "username": "mor_2314",
        "password": "wrongpass"
    }
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code == 401
