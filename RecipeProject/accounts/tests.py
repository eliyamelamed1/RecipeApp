import pytest
import json
from django.contrib.auth import get_user_model

@pytest.fixture
def create_user_fixture():
    User = get_user_model()
    create_user = User.objects.create_user(
        name='User', 
        email='User@gmail.com',
        password='Userpass'
    )
    return create_user

@pytest.fixture
def create_superuser_fixture():
    User = get_user_model()
    create_superuser = User.objects.create_superuser(
        name='SuperUser', 
        email='SuperUser@gmail.com',
        password='SuperUserpass'
    ) 
    return create_superuser

@pytest.mark.django_db
def test_create_user(create_user_fixture):
    simple_user = create_user_fixture
    
    assert simple_user.name == 'User'
    assert simple_user.email == 'User@gmail.com'
    assert simple_user.is_active == True
    assert simple_user.is_staff == False
    assert simple_user.is_superuser == False



@pytest.mark.django_db
def test_create_superuser(create_superuser_fixture):
    admin_user = create_superuser_fixture

    assert admin_user.name == 'SuperUser'
    assert admin_user.email == 'SuperUser@gmail.com'
    assert admin_user.is_active == True
    assert admin_user.is_staff == True
    assert admin_user.is_superuser == True


@pytest.mark.django_db
def test_login_with_email(client,create_user_fixture):
    user = create_user_fixture
    login = client.login(email='User@gmail.com', password='Userpass',)
    assert login == True
    
