"""BookAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Books.views import BookViewSet, FantasyViewSet, GothicFictionViewSet, HistoricalViewSet, NovelViewSet, HistoricalFicViewSet, DystopianViewSet, RomanticViewSet, SelfHelpViewSet, CrimeViewSet, ThrillerViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('Books', BookViewSet)
router.register('Fantasy', FantasyViewSet)
router.register('Southern Gothic', GothicFictionViewSet)
router.register('Historical non-fiction', HistoricalViewSet)
router.register('Novel', NovelViewSet)
router.register('Historical Fiction', HistoricalFicViewSet)
router.register('Dystopian', DystopianViewSet)
router.register('Romantic Novel', RomanticViewSet)
router.register('Self-help', SelfHelpViewSet)
router.register('Crime Novel', CrimeViewSet)
router.register('Thriller', ThrillerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
