from rest_framework.authentication import get_authorization_header

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

import requests


def load_django_setting(setting_name, default_value=None):
    setting_value = getattr(settings, setting_name, default_value)

    if setting_value == None:
        raise ImproperlyConfigured(_(f"Setting {setting_name} is not configured."))
        
    return setting_value


def get_data_from_microservice(request, path):
    try:
        headers = {"Authorization": get_authorization_header(request)}
        r = requests.get(path, headers=headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return err.response.json()

    except Exception as err:
        raise Exception(err)

    return r.json()


def get_user_jwt_from_microservice(username, password):
    try:
        headers = {"Content-Type": "application/json"}
        path = settings.USER_MICROSERVICE_LOGIN_URI
        r = requests.post(
            path, json={"email": username, "password": password}, headers=headers)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        # return err.response.json()
        return None

    except Exception as err:
        # raise Exception(err)
        return None

    return r.json()
