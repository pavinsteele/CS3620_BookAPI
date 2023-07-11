from django.db import models


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.book_name

    book_name = models.CharField(max_length=200)
    book_cat = models.CharField(max_length=200, default='favorites')
    book_desc = models.CharField(max_length=200)
    book_rate = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')
