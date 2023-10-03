import requests

base_url = 'http://localhost:5000'


def signup(email, password):
    url = f'{base_url}/signup'
    data = {'email': email, 'password': password}
    response = requests.post(url, json=data)
    return response


def signin(email, password):
    url = f'{base_url}/signin'
    data = {'email': email, 'password': password}
    response = requests.post(url, json=data)
    return response


def logout(email):
    url = f'{base_url}/logout'
    data = {'email': email}
    response = requests.post(url, json=data)
    return response


if __name__ == '__main__':
    email1 = 'james@gmail.com'
    password1 = 'james37'

    signup_response = signup(email1, password1)
    print('Sign-up response:', signup_response.status_code)
    print(signup_response.json())

    signin_response = signin(email1, password1)
    print('Sign-in response:', signin_response.status_code)
    print(signin_response.json())

    logout_response = logout(email1)
    print('Logout response:', logout_response.status_code)
    print(logout_response.json())
