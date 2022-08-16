from django.contrib import admin
from django.db import models
from .models import Index, About, Cohort, CohortBatch, Register, Staff, Event, News, Announcements, Publications, Contact, Socials


@admin.register(Index, About, Cohort, CohortBatch, Register, Staff, Event, News, Announcements, Publications, Contact, Socials)
class IndexAdmin(admin.ModelAdmin):
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
    team = models.ForeignKey('Staff', on_delete=models.CASCADE)
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    socials = models.ForeignKey('Socials', on_delete=models.CASCADE)
    copyright = models.CharField(max_length=128)


class AboutAdmin(models.Model):
    tab_title = models.CharField(max_length=64)
    tab_info = models.TextField()


class CohortAdmin(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=64)
    programme = models.CharField(max_length=64)


class CohortBatchAdmin(models.Model):
    batch = models.CharField(max_length=64)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)


class RegisterAdmin(models.Model):
    info = models.TextField()


class StaffAdmin(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=64)


class EventAdmin(models.Model):
    date_posted = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=64)
    title = models.CharField(max_length=128)


class NewsAdmin(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=128)
    info = models.TextField()
    date_published = models.DateTimeField(auto_now=True)


class AnnouncementsAdmin(models.Model):
    title = models.CharField(max_length=128)
    date_published = models.DateTimeField(auto_now=True)


class PublicationsAdmin(models.Model):
    title = models.CharField(max_length=64)


class ContactAdmin(models.Model):
    telephone = models.CharField(max_length=16)
    cell_phone = models.CharField(max_length=16)
    email1 = models.CharField(max_length=32)
    email2 = models.CharField(max_length=32)
    map = models.TextField(max_length=128)


class SocialsAdmin(models.Model):
    facebook = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)
    instagram = models.CharField(max_length=128)
    youtube = models.CharField(max_length=128)
