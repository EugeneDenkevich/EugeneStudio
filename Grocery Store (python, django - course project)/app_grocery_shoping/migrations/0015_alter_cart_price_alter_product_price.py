# Generated by Django 4.1.1 on 2022-09-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0014_delete_fruit_delete_milk_and_meat_delete_vegitable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]