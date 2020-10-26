# Generated by Django 3.1.2 on 2020-10-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='decsription',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
