# Generated by Django 2.2.14 on 2020-08-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_upload_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='notes',
            field=models.TextField(max_length=1024),
        ),
    ]
