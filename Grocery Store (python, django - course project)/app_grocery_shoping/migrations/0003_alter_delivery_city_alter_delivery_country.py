# Generated by Django 4.1.1 on 2022-09-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0002_alter_delivery_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
