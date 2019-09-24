from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('information', views.InformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', include('rest_framework.urls')),
    path('/FiltrateSchool/',views.InformationViewSet.FiltrateSchool)
]