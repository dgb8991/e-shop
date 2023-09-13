# Generated by Django 4.2.4 on 2023-09-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.CharField(default='', max_length=255),
        ),
    ]
