from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.db import models
from .models import Index, About, Cohort, CohortBatch, Register, Staff, Event, News, Announcements,  Publications, Contact, Socials


@admin.register(Index)
class IndexAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
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


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = 'tab_title',
    summernote_fields = '__all__'

    tab_title = models.CharField(max_length=64)
    tab_info = models.TextField()


@admin.register(Cohort)
class CohortAdmin(SummernoteModelAdmin):
    list_display = 'name', 'programme'
    summernote_fields = '__all__'

    img = models.ImageField()
    name = models.CharField(max_length=64)
    programme = models.CharField(max_length=64) 


@admin.register(CohortBatch)
class CohortBatchAdmin(SummernoteModelAdmin):
    list_display = list_filter = 'batch',
    summernote_fields = '__all__'

    batch = models.CharField(max_length=64)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)


@admin.register(Register)
class RegisterAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    info = models.TextField()


@admin.register(Staff)
class StaffAdmin(SummernoteModelAdmin):
    list_display = 'name', 'role'
    summernote_fields = '__all__'
    img = models.ImageField()
    name = models.CharField(max_length=64)
    role = models.CharField(max_length=64)


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = 'date_posted', 'location', 'title'
    summernote_fields = '__all__'

    date_posted = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=64)
    title = models.CharField(max_length=128)


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    list_display = 'title', 'info', 'date_published'
    summernote_fields = '__all__'

    img = models.ImageField()
    title = models.CharField(max_length=128)
    info = models.TextField()
    date_published = models.DateTimeField(auto_now=True)


@admin.register(Announcements)
class AnnouncementsAdmin(SummernoteModelAdmin):
    list_display = 'title',
    summernote_fields = '__all__'

    title = models.CharField(max_length=128)
    date_published = models.DateTimeField(auto_now=True)


@admin.register(Publications)
class PublicationsAdmin(SummernoteModelAdmin):
    list_display = 'title', 'url_to_file'
    summernote_fields = '__all__'
    title = models.CharField(max_length=64)
    url_to_file = models.CharField(max_length=128)


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = 'telephone', 'cell_phone', 'email1', 'email2', 'map'
    summernote_fields = '__all__'

    telephone = models.CharField(max_length=16)
    cell_phone = models.CharField(max_length=16)
    email1 = models.CharField(max_length=32)
    email2 = models.CharField(max_length=32)
    map = models.TextField(max_length=128)


@admin.register(Socials)
class SocialsAdmin(SummernoteModelAdmin):
    list_display = 'facebook', 'twitter', 'instagram', 'youtube'
    summernote_fields = '__all__'

    facebook = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)
    instagram = models.CharField(max_length=128)
    youtube = models.CharField(max_length=128)
