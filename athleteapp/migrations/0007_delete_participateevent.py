# Generated by Django 5.0.3 on 2024-07-25 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athleteapp', '0006_remove_participateevent_college'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParticipateEvent',
        ),
    ]