# Generated by Django 2.2.14 on 2020-08-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_auto_20200813_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='notes',
            field=models.TextField(),
        ),
    ]
