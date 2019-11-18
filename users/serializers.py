#from django.utils.dateparse import parse_datetime
from rest_framework import serializers
from users.models import Account
#from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'is_superuser', 'first_name', 'last_name')


class AccountSerializerWithToken(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, user):
        #jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        #jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        #payload = jwt_payload_handler(object)
        #token = jwt_encode_handler(payload)
        #return token
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data['username'],
            #first_name=validated_data['first_name'],
            #last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Account
        fields = ('token', 'username', 'password', 'first_name', 'last_name')
