# Generated by Django 4.1.1 on 2022-09-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0004_alter_delivery_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='day_of_birth',
            field=models.DateTimeField(null=True),
        ),
    ]
