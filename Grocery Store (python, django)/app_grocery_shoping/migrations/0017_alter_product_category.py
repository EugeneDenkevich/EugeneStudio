# Generated by Django 4.1.1 on 2022-09-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0016_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('Vegetables', 'Vegitables'), ('Milk-and-meat', 'Milk and Meat')], max_length=20),
        ),
    ]
