from django.db import models


class Index(models.Model):
    logo = models.ImageField()
    motto = models.CharField(max_length=128)
    about_program_col1 = models.TextField(verbose_name="About Section - Coloumn 1")
    about_program_col2 = models.TextField(verbose_name="About Section - Coloumn 2")
    about_program_col3 = models.TextField(verbose_name="About Section - Coloumn 3")
    about_program_col4 = models.TextField(verbose_name="About Section - Coloumn 4")
    our_scholars = models.TextField()
    how_it_works_url = models.CharField(max_length=128)
    announcements = models.TextField()
    copyright = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Index'

    def __str__(self):
        return "Index"

class About(models.Model):
    tab_title = models.CharField(max_length=64)
    tab_info = models.TextField()

    class Meta:
        verbose_name_plural = 'About'



class Cohort(models.Model):
    img = models.ImageField(upload_to="cohort", verbose_name="Profile Picture")
    name = models.CharField(max_length=64)
    programme = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Cohort'
        


class CohortBatch(models.Model):
    batch = models.CharField(max_length=64)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cohort Batches'


class Register(models.Model):
    info = models.TextField()

    class Meta:
        verbose_name_plural = 'Register'

    def __str__(self):
        return "Information About Registration"


class Staff(models.Model):
    img = models.ImageField(upload_to="staff",verbose_name="Profile Picture")
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
    img = models.ImageField(verbose_name="Thumbnail")
    title = models.CharField(max_length=128)
    info = models.TextField()
    date_published = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'News'


class Announcements(models.Model):
    title = models.CharField(max_length=128)
    date_published = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Announcements'


class Publications(models.Model):
    title = models.CharField(max_length=64)
    url_to_file = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Publications'


class Contact(models.Model):
    telephone = models.CharField(max_length=16)
    cell_phone = models.CharField(max_length=16)
    address = models.TextField(max_length=256)
    email1 = models.CharField(max_length=32, verbose_name="first email")
    email2 = models.CharField(max_length=32, verbose_name="second email")
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
