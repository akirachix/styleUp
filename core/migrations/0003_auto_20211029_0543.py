# Generated by Django 3.2.4 on 2021-10-29 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
    ]
