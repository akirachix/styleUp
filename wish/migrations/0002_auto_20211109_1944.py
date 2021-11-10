# Generated by Django 3.2.4 on 2021-11-09 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_category'),
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='wishitem',
            name='wish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wish.wish'),
        ),
    ]
