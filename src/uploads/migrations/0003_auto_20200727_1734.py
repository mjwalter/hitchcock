# Generated by Django 2.2.14 on 2020-07-27 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20200727_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('identifer', models.CharField(help_text='barcode, ISBN, etc.', max_length=512)),
                ('form', models.CharField(choices=[('digitized', 'Digitized'), ('born_digital', 'Born Digital')], default='digitized', max_length=16)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='text',
            name='created',
        ),
        migrations.RemoveField(
            model_name='text',
            name='form',
        ),
        migrations.RemoveField(
            model_name='text',
            name='id',
        ),
        migrations.RemoveField(
            model_name='text',
            name='identifer',
        ),
        migrations.RemoveField(
            model_name='text',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='text',
            name='title',
        ),
        migrations.AddField(
            model_name='text',
            name='upload_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uploads.Upload'),
            preserve_default=False,
        ),
    ]
