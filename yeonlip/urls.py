from django.urls import path, include
from rest_framework.routers import DefaultRouter

from yeonlip import views

router = DefaultRouter()
router.register('yeonlips', views.YeonlipViewSet)
router.register('units', views.UnitViewSet)

app_name = 'yeonlip'

urlpatterns = [
    path('', include(router.urls))
]
