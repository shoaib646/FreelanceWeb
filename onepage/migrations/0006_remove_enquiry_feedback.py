# Generated by Django 4.1.5 on 2023-05-31 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0005_alter_enquiry_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='feedback',
        ),
    ]
