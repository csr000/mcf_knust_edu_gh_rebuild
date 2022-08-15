from django.db import models


class Index(models.Model):
    logo = models.ImageField()
    motto = models.CharField(max_length=128)
    about_program_col1 = models.TextField()
    about_program_col2 = models.TextField()
    about_program_col3 = models.TextField()
    about_program_col4 = models.TextField()
    about_program_col4 = models.TextField()
    our_scholars = models.TextField()
    how_it_works_url = models.CharField(max_length=128)
    announcements = models.TextField()
    copyright = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Index'


class About(models.Model):
    tab_title = models.CharField(max_length=64)
    tab_info = models.TextField()

    class Meta:
        verbose_name_plural = 'About'


class Cohort(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=64)
    programme = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Cohort'


class Register(models.Model):
    info = models.TextField()

    class Meta:
        verbose_name_plural = 'Register'


class Staff(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Staff'


class Event(models.Model):
    date_posted = models.DateTimeField()
    location = models.CharField(max_length=64)
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Event'


class News(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=128)
    info = models.TextField()
    date_published = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'


class Announcements(models.Model):
    title = models.CharField(max_length=128)
    date_published = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Announcements'


class Publications(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Publications'


class Contact(models.Model):
    telephone = models.CharField(max_length=16)
    cell_phone = models.CharField(max_length=16)
    email1 = models.CharField(max_length=32)
    email2 = models.CharField(max_length=32)
    map = models.TextField(max_length=128)

    class Meta:
        verbose_name_plural = 'Contact'


class Socials(models.Model):
    facebook = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)
    instagram = models.CharField(max_length=128)
    youtube = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Socials'
