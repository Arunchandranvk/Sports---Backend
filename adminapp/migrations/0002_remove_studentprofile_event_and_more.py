# Generated by Django 4.2.5 on 2024-05-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='event',
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='adm_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='ph_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
