# Generated by Django 4.0.5 on 2022-08-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_contact_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(max_length=256),
        ),
    ]