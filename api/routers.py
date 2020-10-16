from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'farms', views.FarmViewSet)
router.register(r'cats', views.CatViewSet)
router.register(r'owners', views.OwnerViewSet)
