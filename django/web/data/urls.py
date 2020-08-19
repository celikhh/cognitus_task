from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'data', DataViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('train/', trigger_train),
    path('predict/<str:user_text>', trigger_predict)
]
