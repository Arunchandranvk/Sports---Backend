# Generated by Django 4.2.5 on 2024-05-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_studentprofile_adm_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
