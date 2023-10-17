from rest_framework import serializers

class UserInformationSerializer(serializers.Serializer):
    """
    User serializer to show user information
    """

    username = serializers.CharField()