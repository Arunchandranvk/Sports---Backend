# Generated by Django 5.0.3 on 2024-07-25 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athleteapp', '0005_alter_participateevent_college'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participateevent',
            name='college',
        ),
    ]
