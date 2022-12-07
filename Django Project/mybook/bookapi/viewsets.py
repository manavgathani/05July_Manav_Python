from rest_framework import viewsets
from . import models
from . import serializers


class bookviews(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.bookserializer