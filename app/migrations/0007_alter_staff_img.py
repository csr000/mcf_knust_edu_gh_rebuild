# Generated by Django 4.0.5 on 2022-08-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_index_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='img',
            field=models.ImageField(upload_to='staff'),
        ),
    ]
