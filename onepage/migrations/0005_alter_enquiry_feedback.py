# Generated by Django 4.1.5 on 2023-05-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onepage', '0004_alter_enquiry_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='feedback',
            field=models.CharField(blank=True, choices=[('Probably Right', 'Probably Right'), ('High', 'High'), ('Low', 'Low')], max_length=265),
        ),
    ]
