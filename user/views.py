from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


from user import models
from user import serializers

from rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):
    queryset = models.User.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.UserSerializer
    http_method_names = ['get', 'put', 'delete']
    queryset = models.User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^first_name', '^last_name', 'birth_date', 'year_of_experience', 'address', 'preferred_language')
    ordering_fields = ('date_joined', )
