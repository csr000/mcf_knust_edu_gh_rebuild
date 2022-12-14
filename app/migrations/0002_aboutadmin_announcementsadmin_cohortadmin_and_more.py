# Generated by Django 4.0.5 on 2022-08-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_title', models.CharField(max_length=64)),
                ('tab_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncementsAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date_published', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CohortAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=64)),
                ('programme', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ContactAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=16)),
                ('cell_phone', models.CharField(max_length=16)),
                ('email1', models.CharField(max_length=32)),
                ('email2', models.CharField(max_length=32)),
                ('map', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='EventAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='NewsAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=128)),
                ('info', models.TextField()),
                ('date_published', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationsAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialsAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=128)),
                ('twitter', models.CharField(max_length=128)),
                ('instagram', models.CharField(max_length=128)),
                ('youtube', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StaffAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=64)),
                ('role', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='announcements',
            options={'verbose_name_plural': 'Announcements'},
        ),
        migrations.AlterModelOptions(
            name='cohort',
            options={'verbose_name_plural': 'Cohort'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='index',
            options={'verbose_name_plural': 'Index'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='publications',
            options={'verbose_name_plural': 'Publications'},
        ),
        migrations.AlterModelOptions(
            name='register',
            options={'verbose_name_plural': 'Register'},
        ),
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name_plural': 'Socials'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'Staff'},
        ),
    ]
