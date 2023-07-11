from rest_framework import serializers
from .models import Item


class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Item
        fields = ['id', 'book_name', 'book_cat', 'book_desc', 'book_rate', 'image']
