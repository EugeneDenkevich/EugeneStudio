# Generated by Django 4.1.1 on 2022-09-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0012_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=4)),
                ('company', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads')),
                ('category', models.CharField(choices=[('f', 'Fruits'), ('v', 'Vegitables'), ('m', 'Milk and Meat')], max_length=1)),
            ],
        ),
    ]
