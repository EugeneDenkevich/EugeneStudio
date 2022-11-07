# Generated by Django 4.1.1 on 2022-09-16 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_grocery_shoping', '0006_alter_user_day_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milk_and_Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=4)),
                ('company', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Vegitable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=4)),
                ('company', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Fruit',
        ),
    ]