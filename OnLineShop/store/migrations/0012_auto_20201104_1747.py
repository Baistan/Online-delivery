# Generated by Django 3.1.2 on 2020-11-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201103_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
