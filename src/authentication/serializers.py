from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["user_id",
                  "email",
                  "first_name",
                  "last_name",
                  "password",
                  ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
