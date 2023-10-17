from django.urls import path

from shared_security.api.views import users as users_views

urlpatterns = [
    path('user', users_views.UserViewSet.as_view({'get': 'retrieve_user'}), name='users'),
]