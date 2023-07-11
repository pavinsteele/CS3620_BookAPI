from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Item
from django.template import loader


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Fantasy')
    serializer_class = BookSerializer


class GothicFictionViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Southern Gothic')
    serializer_class = BookSerializer


class HistoricalViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Historical non-fiction')
    serializer_class = BookSerializer


class NovelViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Novel')
    serializer_class = BookSerializer


class HistoricalFicViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Historical Fiction')
    serializer_class = BookSerializer


class DystopianViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Dystopian')
    serializer_class = BookSerializer


class RomanticViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Romantic Novel')
    serializer_class = BookSerializer


class SelfHelpViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Self-help')
    serializer_class = BookSerializer


class CrimeViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Crime Novel')
    serializer_class = BookSerializer


class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(book_cat='Thriller')
    serializer_class = BookSerializer