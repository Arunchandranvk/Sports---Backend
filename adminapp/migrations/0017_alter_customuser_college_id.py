# Generated by Django 5.0.3 on 2024-08-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_alter_winner_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='college_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
