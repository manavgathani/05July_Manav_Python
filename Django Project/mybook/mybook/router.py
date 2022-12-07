from rest_framework import routers
from bookapi.viewsets import bookviews

router = routers.DefaultRouter()
router.register('book',bookviews) 