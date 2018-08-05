from django.conf.urls import url, include
from django.contrib import admin
from .views import LanguageView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', LanguageView)

urlpatterns = [
	url(r'^', include(router.urls)),
]