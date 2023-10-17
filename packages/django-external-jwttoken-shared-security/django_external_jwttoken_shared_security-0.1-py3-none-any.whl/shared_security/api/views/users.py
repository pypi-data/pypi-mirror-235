from django.contrib.auth import get_user_model
from django.db.models import ObjectDoesNotExist

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from shared_security.api.serializers.users import UserInformationSerializer
from shared_security.api.serializers.errors import ErrorSerializer


class UserViewSet(viewsets.ViewSet):
    """
    User registration and edition endpoints
    """

    @extend_schema(
        methods=["GET"],
        responses={
            200: UserInformationSerializer,
            403: ErrorSerializer,
            422: ErrorSerializer
        },
        summary="Returns the information of a given user from token"
                         )
    @action(detail=True, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def retrieve_user(self, request, **kwargs):
        """
        This endpoint returns the information of a given user from token obtained from auth
        microservice
        """

        user = request.user

        user_info_serializer = UserInformationSerializer({
            "username": user.username,
        })

        return Response(user_info_serializer.data, status=200)