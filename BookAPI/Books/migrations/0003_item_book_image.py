# Generated by Django 2.2 on 2023-07-11 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20230709_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='book_image',
            field=models.CharField(default='https://cor-cdn-static.bibliocommons.com/assets/default_covers/icon-book-93409e4decdf10c55296c91a97ac2653.png', max_length=500),
        ),
    ]
