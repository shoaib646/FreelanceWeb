# Generated by Django 4.1.5 on 2023-05-31 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0007_feedbackmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='feedback',
            field=models.CharField(choices=[('Probably Right', 'Probabaly Right'), ('High', 'High'), ('Low', 'Low')], default='How accurate does this  look to you', max_length=20),
        ),
    ]
