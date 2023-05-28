# Generated by Django 3.2.15 on 2022-08-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('uuid', models.UUIDField(default=None, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60, verbose_name='email address')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name')),
                ('ref_no', models.CharField(blank=True, max_length=8, null=True, verbose_name='Student Reference Number')),
                ('department', models.CharField(blank=True, max_length=255, null=True, verbose_name='Department')),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active status')),
                ('staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin assets.', verbose_name='Staff status')),
                ('admin', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Superuser status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]