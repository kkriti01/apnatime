from rest_framework import viewsets, response
from rest_framework import filters, permissions
from rest_framework.parsers import FormParser, MultiPartParser

from user import models
from user import serializers

from rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):
    queryset = models.User.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.UserSerializer
    http_method_names = ['get', 'put', 'delete', 'patch']
    queryset = models.User.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^first_name', '^last_name', 'birth_date', 'year_of_experience', 'address', 'preferred_language')
    ordering_fields = ('date_joined', )


