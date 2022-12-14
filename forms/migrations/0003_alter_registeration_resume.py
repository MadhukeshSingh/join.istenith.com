# Generated by Django 4.0.8 on 2022-12-12 06:27

import django.core.files.storage
import django.core.validators
from django.db import migrations, models
import forms.models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_alter_registeration_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='resume',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=pathlib.PurePosixPath('/home/lucifer/join.istenith.com/media')), upload_to='resumes/', validators=[forms.models.file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])]),
        ),
    ]
