from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from user import models


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=False)
    password1 = serializers.CharField(write_only=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    year_of_experience = serializers.DecimalField(max_digits=5, decimal_places=2,  default=0.0)
    address = serializers.CharField(required=False)
    profile_picture = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    preferred_language = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'year_of_experience': self.validated_data.get('year_of_experience', ''),
            'address': self.validated_data.get('address', ''),
            'profile_picture': self.validated_data.get('profile_picture', ''),
            'preferred_language': self.validated_data.get('preferred_language', ''),
            'birth_date': self.validated_data.get('birth_date', ''),

        }


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'email', 'birth_date', 'year_of_experience', 'address', 'profile_picture',
                  'preferred_language')
