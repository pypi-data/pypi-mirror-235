from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from shared_security.helpers import (
    get_user_jwt_from_microservice, load_django_setting)
from shared_security.models import UserExternalData

import jwt


def check_user_admin_role(user_data):
    if user_data != None and "rol" in user_data and "id" in user_data["rol"] and user_data["rol"]["id"] == 12:
        return True
    elif user_data == None:
        return True

    return False


def create_new_user(user_model, username, user_data=None):
    user = user_model.objects.create(username=username)
    # TODO: at the moment harcoded to the user rol with id 12
    if check_user_admin_role(user_data):
        user.is_staff = True
        user.is_superuser = True
        user.save()
    
    if user_data:
        UserExternalData.objects.create(
            user_rel=user, external_id=user_data["id"], fullname=user_data["fullname"])
    return user


def update_user(user):
    user.is_superuser = True
    user.is_staff = True
    user.save()


class ExternalTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'  # token type

    def get_data_from_token(self, key):
        JWT_SECRET_KEY = load_django_setting('JWT_SECRET_KEY')
        decoded_token = jwt.decode(
            key, JWT_SECRET_KEY, algorithms=["HS256"])
        return {
            "user_id": decoded_token["id"]
        }

    def authenticate_credentials(self, key):
        # decode JWT.
        try:
            token_data = self.get_data_from_token(key)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        user_model = get_user_model()
        SECURITY_USE_PERSISTENT_USERS = load_django_setting(
            'SECURITY_USE_PERSISTENT_USERS', True)
        # TODO: at the moment harcoded to the root user
        # add request to get user data from id or token
        if SECURITY_USE_PERSISTENT_USERS:
            try:
                # TODO: at the moment all user logged at least one time is considered as a superuser
                user = user_model.objects.get(username="root")
                update_user(user)
            except user_model.DoesNotExist:
                user = create_new_user(user_model, "root")
        else:
            user = user_model(
                username="root", is_superuser=True, is_staff=True)
        return user, key


class ExternalAuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        # Get the user information from external jwt auth microservice if he can be authenticated
        response = get_user_jwt_from_microservice(username, password)
        if response is None:
            return None

        login_data = response['user']
        user_model = get_user_model()
        SECURITY_USE_PERSISTENT_USERS = load_django_setting(
            'SECURITY_USE_PERSISTENT_USERS', True)
        
        if SECURITY_USE_PERSISTENT_USERS:
            try:
                # TODO: at the moment all user logged at least one time is considered as a superuser
                user = user_model.objects.get(username=login_data["username"])
                update_user(user)
            except user_model.DoesNotExist:
                user = create_new_user(
                    user_model, login_data["username"], login_data)
        else:
            # user = user_model(pk=1,
            #     username=login_data["username"], is_superuser=True, is_staff=True)
            return None
        return user

    def get_user(self, user_id):
        user_model = get_user_model()
        
        SECURITY_USE_PERSISTENT_USERS = load_django_setting(
            'SECURITY_USE_PERSISTENT_USERS', True)
        
        if SECURITY_USE_PERSISTENT_USERS:
            try:
                return user_model.objects.get(pk=user_id)
            except user_model.DoesNotExist:
                return None
        else:
            return None
