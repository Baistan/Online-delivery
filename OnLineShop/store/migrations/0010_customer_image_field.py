# Generated by Django 3.1.2 on 2020-11-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20201103_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image_field',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
