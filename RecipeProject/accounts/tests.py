import pytest

@pytest.fixture
def user_creation_fixture(client):
    url = "/auth/users/"
    data = {"email": "john@gmail.com" ,"name": "john", "password": "56156asd", "re_password": "56156asd"}
    user_created = client.post(url, data)

    assert user_created.status_code == 201
    return user_created

@pytest.fixture
def user_email_login_fixture(client, user_creation_fixture):
    url = "/auth/jwt/create/"
    data = {"email": "john@gmail.com" , "password": "56156asd"}
    user_email_login = client.post(url, data)

    assert user_email_login.status_code == 200
    return user_email_login


@pytest.mark.django_db
def test_user_signup(user_creation_fixture):
    user_created = user_creation_fixture

    assert user_created.status_code == 201

@pytest.mark.django_db
def test_user_email_login(user_email_login_fixture):
    user_logged_in = user_email_login_fixture

    assert user_logged_in.status_code == 200
