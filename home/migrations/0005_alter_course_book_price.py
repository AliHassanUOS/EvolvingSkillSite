# Generated by Django 3.2 on 2021-05-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210515_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Book_price',
            field=models.IntegerField(null=True),
        ),
    ]